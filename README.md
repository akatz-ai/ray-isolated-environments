# Using isolated environments with Ray and UV

This repository shows how to use isolated UV environments in a single Ray application.

## ray-core

Switch into the `ray-core` directory and run the example with `uv run
main.py`. This will run the Ray driver in the environment defined by
`ray-core/pyproject.toml`, the first actor in the environment defined
by `ray-core/env1/pyproject.toml` and the second actor in the
environment defined by `ray-core/env2/pyproject.toml`.

You should see an output like
```
% uv run main.py
2025-04-29 15:28:47,431	INFO worker.py:1888 -- Started a local Ray instance.
(raylet) warningwarning: `VIRTUAL_ENV=.venv` does not match the project environment path `env2/.venv` and will be ignored
(raylet) : `VIRTUAL_ENV=.venv` does not match the project environment path `env1/.venv` and will be ignored
(SecondActor pid=27857) I'm the second actor and my numpy version is 2.2.5
(FirstActor pid=27856) I'm the first actor and my numpy version is 1.26.4
['Hello', 'World']
```

*Note:* The Ray and Python versions in both environments need to agree (this is to ensure
that data passed between the different environments is consistent), other packages can be
different. If Python objects are passed between the environments, they need to be compatible
too -- this will be the case for primitive Python types like strings, dicts, lists etc. and
also often for user defined types unless their representation changed between the different
package versions (e.g. if a field got added or removed).
