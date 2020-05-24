import click
import unicodedata


@click.group()
def main():
    pass


@click.command()
@click.argument("character")
def name(character):
    print(f"You want the name of: {character}")
    print(unicodedata.name(character))


@click.command()
@click.argument("charname")
def find(charname):
    print(f"You want to find: {charname}")
    print(unicodedata.lookup(charname))


main.add_command(name)
main.add_command(find)
