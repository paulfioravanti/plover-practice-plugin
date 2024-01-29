import os
import random

def random_number(ctx, argument):
    low, high = [int(arg) for arg in argument.split(":")]
    number = random.randint(low, high)

    action = ctx.new_action()
    action.text = str(number)
    return action

def get_env_var(ctx, argument):
    shell = os.getenv("SHELL", "bash").split("/")[-1]
    env_var = os.popen(f"{shell} -ic 'echo {argument}'").read().strip()

    action = ctx.new_action()
    action.text = env_var
    return action
