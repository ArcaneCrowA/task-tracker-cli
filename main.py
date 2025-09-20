import typer

from commands import (
    add_command,
    delete_command,
    list_command,
    mark_command,
    update_command,
)

app = typer.Typer(no_args_is_help=True)


@app.command()
def add(description: str):
    add_command.add(description=description)


@app.command()
def update(id: int, description: str):
    res = update_command.update(id, description)
    check(res)


@app.command()
def delete(id: int):
    delete_command.delete(id)


list_app = typer.Typer()


@list_app.callback(invoke_without_command=True)
def list_callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        list_all()


@list_app.command("all")
def list_all():
    list_command.list(filter="all")


@list_app.command("todo")
def list_todo():
    list_command.list(filter="todo")


@list_app.command("done")
def list_done():
    list_command.list(filter="done")


@list_app.command("in-progress")
def list_in_progress():
    list_command.list(filter="in-progress")


mark_app = typer.Typer()


@mark_app.command("done")
def mark_done(id: int):
    res = mark_command.mark(status="done", id=id)
    check(res)


@mark_app.command("todo")
def mark_todo(id: int):
    res = mark_command.mark(status="todo", id=id)
    check(res)


@mark_app.command("in-progress")
def mark_in_progress(id: int):
    res = mark_command.mark(status="in-progress", id=id)
    check(res)


def check(res):
    if res == 0:
        print("No file")
        typer.Exit()
    elif res == 1:
        print("id not found")
        typer.Exit()


app.add_typer(list_app, name="list")
app.add_typer(mark_app, name="mark")

if __name__ == "__main__":
    app()
