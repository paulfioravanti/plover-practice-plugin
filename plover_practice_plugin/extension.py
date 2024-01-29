import os
from plover.registry import registry

class PracticePlugin:
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        registry.register_plugin("meta", "get_env_var", self._get_env_var)

    def stop(self):
        pass

    def _get_env_var(self, ctx, argument):
        shell = os.getenv("SHELL", "bash").split("/")[-1]
        env_var = os.popen(f"{shell} -ic 'echo {argument}'").read().strip()

        action = ctx.new_action()
        action.text = env_var
        return action
