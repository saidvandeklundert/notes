import typer
from rich import print

app = typer.Typer(help="Superduper.")

pretty_data = {"1": 1, "2": [1, 2, 3], "bool": False}


@app.command()
def cli(cli: str):
    print(f"running {cli}")
    print(pretty_data)


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"CU later {name}!")


if __name__ == "__main__":
    app()
