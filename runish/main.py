import click
import unicodedata


@click.group()
def main():
    pass


@click.command()
@click.argument("character")
def name(character):
    print(name_character(character))


@click.command()
@click.argument("charname")
def find(charname):
    print(find_charname(charname))


def find_charname(charname):
    return unicodedata.lookup(charname)


def name_character(character):
    return unicodedata.name(character)


main.add_command(name)
main.add_command(find)
