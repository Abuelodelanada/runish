import click


@click.command()
@click.argument("find")
def main(**kwargs):
    find = kwargs['find']
    print(f"You want to find: {find}")
