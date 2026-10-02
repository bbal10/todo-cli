# todo-cli

A command-line todo app built with Python and [Click](https://click.palletsprojects.com/).

> **Status:** early development. The `todo` command currently only prints a greeting; task management commands are not implemented yet.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Installation

```sh
git clone <repo-url>
cd todo-cli
uv sync
```

This creates a `.venv` and installs the project in editable mode, along with its dependencies.

## Usage

Run through `uv`:

```sh
uv run todo
```

Or activate the virtual environment first:

```sh
source .venv/bin/activate
todo
```

Current output:

```
Hello from todo-cli!
```

## Project structure

```
todo-cli/
├── pyproject.toml        # project metadata and `todo` entry point
├── src/
│   └── todo_cli/
│       ├── __init__.py
│       └── main.py       # Click command definitions (`cli`)
└── uv.lock
```

The `todo` console script is declared in `pyproject.toml`:

```toml
[project.scripts]
todo = "todo_cli.main:cli"
```

## Development

After editing `pyproject.toml` (for example, to change the entry point), re-run `uv sync` so the `todo` script is regenerated.

## Roadmap

- [ ] `todo add <task>`
- [ ] `todo list`
- [ ] `todo done <id>`
- [ ] `todo remove <id>`
- [ ] Persistent storage
