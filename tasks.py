from base import base_tasks
from invoke import Collection, task


@task
def print_outer_default(ctx):
    """
    Show the contents of the config available to the outer level
    """
    print(ctx.base_config)
    print(ctx.outer_config)

ns = Collection(print_outer_default, base_tasks)

"""
Tried different methods
Collection()
.add_task(print_outer_default)
.add_collection(base_tasks.ns)
"""