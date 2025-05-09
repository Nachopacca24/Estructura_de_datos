"CLick example"

import click
from datetime import datetime


@click.group()
def cli():
    pass



@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@cli.command()
def timenow():
    print(f'\n{datetime.now()}\n')

@cli.command()
@click.option("--input1", prompt="Ingresa el primer número", type=int, help="El primer número para sumar.")
@click.option("--input2", prompt="Ingresa el segundo número", type=int, help="El segundo número para sumar.")
def add(input1, input2):
    """Suma dos números proporcionados por el usuario."""
    resultado = input1 + input2
    print(f'\nResultado: {resultado}\n')

if __name__ == '__main__':
    cli()