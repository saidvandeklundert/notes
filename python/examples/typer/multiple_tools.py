import typer
from rich import print

app = typer.Typer(help="This CLI allows you to interface with multiple tools.")

pretty_data = {"1": 1, "2": [1, 2, 3], "bool": False}


@app.command()
def tool_one(argument: str):
    print(f"running {argument}")
    print(pretty_data)


@app.command()
def tool_two(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"CU later {name}!")


@app.command()
def tool_three(name: str = "dogbird", formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"CU later {name}!")


if __name__ == "__main__":
    app()
