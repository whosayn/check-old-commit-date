# check-old-commit-date

A prepare-commit-msg hook for [pre-commit](https://github.com/pre-commit/pre-commit)
intended to prevent contributors from pushing commits with old dates.


### Configuring with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/whosayn/check-old-commit-date
    rev: v0.0.1
    hooks:
    -   id: check-old-commit-date
```

and install prepare-commit-msg hooks using
```
pre-commit install --hook-type prepare-commit-msg
```
