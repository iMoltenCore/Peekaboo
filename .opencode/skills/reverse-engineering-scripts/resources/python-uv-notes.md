# Python + uv Notes

Use `uv` for dependency management and execution.

## Quick start
```bash
uv venv
uv pip install -r requirements.txt
uv run python scripts/extract_strings.py --file <path>
```

## Tips
- Prefer stdlib when possible.
- Add non-bundled dependencies to `pyproject.toml` under `code-agent`.
