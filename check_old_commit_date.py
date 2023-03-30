import re
import sys
import textwrap

from datetime import datetime

_COMMIT_DATE_REGEX = re.compile(r"^# Date:\s{2,}(.+)$")
_GIT_DATE_FORMAT = "%a %b %d %H:%M:%S %Y %z"
_ERROR_MESSAGE = textwrap.dedent("""
                            The commit date is more than a day old. Please run:

                            \t`git commit --amend --no-edit --reset-author`

                            to update the commit date.
                             """)

def _commit_date_is_expired(commit_date: str) -> bool:
    commit_date = datetime.strptime(commit_date, _GIT_DATE_FORMAT)
    current_date = datetime.now(commit_date.tzinfo)
    elapsed_time = current_date - commit_date
    return elapsed_time.days > 0

def _get_commit_date(commit_msg_file):
    with open(commit_msg_file, "r") as fh:
        if any((match := _COMMIT_DATE_REGEX.match(line)) for line in fh.readlines()):
            return match.group(1)
    return ""


def main() -> int:
    commit_msg_file = sys.argv[1]
    if not (commit_date := _get_commit_date(commit_msg_file)):
        return 0

    if _commit_date_is_expired(commit_date):
        print(_ERROR_MESSAGE)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
