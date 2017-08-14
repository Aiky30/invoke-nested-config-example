from invoke import Collection, task

@task
def print_base_default(ctx):
    """
    Show the contents of the config available to the inner / base level
    """
    print(ctx.base_config)
    print(ctx.outer_config)

ns = Collection(print_base_default)

ns.configure({
    'base_config': "Default config value"
})