# Python project template

A starting point for Python projects, set up with:

- **[uv](https://docs.astral.sh/uv/)** for the virtual environment, dependencies and lockfile
- **[Ruff](https://docs.astral.sh/ruff/)** for linting and formatting
- **[pytest](https://docs.pytest.org/)** with coverage for tests
- **[mypy](https://mypy.readthedocs.io/)** for type checking
- **[pre-commit](https://pre-commit.com/)** to run checks before every commit
- **GitHub Actions** to run the same checks on every push
- **VS Code settings** for format-on-save with Ruff and Pylance type checking

## Getting started

```bash
uv sync                      # create .venv and install everything
uv run pre-commit install    # enable the pre-commit hooks
cp .env.example .env         # then add your real secrets to .env
uv run my-project            # run the example entry point
```

## Everyday commands

| Task | Command |
|---|---|
| Add a package | `uv add pandas` |
| Add a dev-only tool | `uv add --dev <package>` |
| Run tests with coverage | `uv run pytest --cov` |
| Type check | `uv run mypy src` |
| Lint and format | `uv run ruff check --fix .` and `uv run ruff format .` |
| Update pre-commit hooks | `uv run pre-commit autoupdate` |

## Using this template for a new project

1. Rename `src/my_project/` to your package name (lowercase, underscores).
2. In `pyproject.toml`, update `name`, `description` and the `[project.scripts]` entry.
3. Update the import in `tests/test_basic.py`.
4. Run `uv sync` to refresh the lockfile.

## Project layout

```
.
├── .github/workflows/ci.yml   # CI: lint, format, type check, tests
├── .vscode/settings.json      # editor settings
├── src/my_project/            # your code
├── tests/                     # your tests
├── .env.example               # names of the secrets the project needs
├── .pre-commit-config.yaml
└── pyproject.toml             # dependencies and tool settings
```

Recommended VS Code extensions: Python, Pylance, Ruff, Jupyter, autoDocstring, Even Better TOML, GitLens.
