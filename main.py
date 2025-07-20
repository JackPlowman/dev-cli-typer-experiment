import typer

app = typer.Typer()


@app.command()
def main(name: str):
    print(f"Hello {name}")

@app.command()
def launch():
    typer.echo("Launching the application...")
    typer.launch("https://github.com/JackPlowman/dev-cli-typer-experiment")

if __name__ == "__main__":
    app()