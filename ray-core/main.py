import ray

ray.init()

@ray.remote(runtime_env={"py_executable": "uv run --project env1/"})
class FirstActor:
    def __init__(self):
        import numpy
        print(f"I'm the first actor and my numpy version is {numpy.__version__}")

    def pingpong(self, x):
        return x

@ray.remote(runtime_env={"py_executable": "uv run --project env2/"})
class SecondActor:
    def __init__(self):
        import numpy
        print(f"I'm the second actor and my numpy version is {numpy.__version__}")

    def pingpong(self, x):
        return x

actor1 = FirstActor.remote()
actor2 = SecondActor.remote()

print(ray.get([actor1.pingpong.remote("Hello"), actor2.pingpong.remote("World")]))
