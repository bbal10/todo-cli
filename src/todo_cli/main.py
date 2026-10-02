import json
import secrets

import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("task", type=click.STRING)
def add(task):
    with open("data.json", "r") as f:
        data = json.load(f)

    task_id = secrets.token_hex(2)[:3]
    data["todos"].append({"id": task_id, "task": task, "done": False})
    with open("data.json", "w") as f:
        json.dump(data, f)
    click.echo(f"Adding a new task: {task}")


@cli.command()
def list():
    click.echo("Tasks list:")
    with open("data.json", "r") as f:
        data = json.load(f)
    for task in data["todos"]:
        click.echo(
            f"{task['id']}: {task['task']} | {'done' if task['done'] else 'pending'}"
        )


@cli.command()
@click.argument("task_id", type=click.STRING)
def delete(task_id):
    click.echo("Deleting a task...")
    with open("data.json", "r") as f:
        data = json.load(f)
    data["todos"] = [task for task in data["todos"] if task["id"] != task_id]
    with open("data.json", "w") as f:
        json.dump(data, f)
    click.echo(f"Task {task_id} deleted.")


@cli.command()
@click.argument("task_id", type=click.STRING)
def done(task_id):
    with open("data.json", "r") as f:
        data = json.load(f)
    for task in data["todos"]:
        if task["id"] == task_id:
            task["done"] = True
            break
    with open("data.json", "w") as f:
        json.dump(data, f)
    click.echo(f"Task {task_id} marked as done.")
