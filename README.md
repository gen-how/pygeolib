# pytemplate

A Python package template repository.

## Usage

1. Changes the package name from `src/pytemplate/` to `src/<your-package-name>/`
2. Edits the package information in `pyproject.toml`
3. Edits this `README.md`

There are some optional folders not included in this repository that can be created manually if needed.

- `docs/` : additional documents.
- `data/` : other resources.
- `scripts/` : shell scripts, batch files, etc.

## Generating distribution archives

```shell
python -m pip install --upgrade build
```

Run the command from the same directory where `pyproject.toml` is located:

```shell
python -m build
```
