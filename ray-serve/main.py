from ray import serve
from ray.serve.handle import DeploymentHandle


@serve.deployment
class LanguageClassifer:
    def __init__(
        self, spanish_responder: DeploymentHandle, french_responder: DeploymentHandle
    ):
        self.spanish_responder = spanish_responder
        self.french_responder = french_responder

    async def __call__(self, http_request):
        request = await http_request.json()
        language, name = request["language"], request["name"]

        if language == "spanish":
            response = self.spanish_responder.say_hello.remote(name)
        elif language == "french":
            response = self.french_responder.say_hello.remote(name)
        else:
            return "Please try again."

        return await response


@serve.deployment(ray_actor_options={"runtime_env": {"py_executable": "uv run --project env1"}})
class SpanishResponder:
    def say_hello(self, name: str):
        import emoji
        return emoji.emojize(f"Hola {name} :thumbs_up: (version {emoji.__version__})")


@serve.deployment(ray_actor_options={"runtime_env": {"py_executable": "uv run --project env2"}})
class FrenchResponder:
    def say_hello(self, name: str):
        import emoji
        return emoji.emojize(f"Bonjour {name} :thumbs_up: (version {emoji.__version__}")


spanish_responder = SpanishResponder.bind()
french_responder = FrenchResponder.bind()
language_classifier = LanguageClassifer.bind(spanish_responder, french_responder)

