# ray-isolated-environments

## ray-core

Run the example with `uv run main.py`. This will run the Ray driver in the
environment defined by `ray-core/pyproject.toml`, the first actor in the
environment defined by `ray-core/env1/pyproject.toml` and the second actor
in the environment defined by `ray-core/env2/pyproject.toml`.
