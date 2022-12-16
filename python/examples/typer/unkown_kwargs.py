import typer
from rich import print

app = typer.Typer()


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def main(ctx: typer.Context):
    kwargs = {}
    for extra_arg in ctx.args:
        print(f"Got extra arg: {extra_arg}")

    i = 0
    while i < len(ctx.args):
        if ctx.args[i].startswith("--"):
            name = ctx.args[i][2:].replace("-", "_")
            value = ctx.args[i + 1]
            kwargs[name] = value
            i = i + 2
        else:
            raise Exception(f"failed to parse {ctx.args}")
    print(kwargs)


if __name__ == "__main__":
    app()
