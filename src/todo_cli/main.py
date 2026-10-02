import json
from pathlib import Path

import click


def load_tasks(path: Path) -> list[dict]:
    """Baca daftar task. Buat file kosong otomatis kalau belum ada."""
    if not path.exists():
        save_tasks(path, [])
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8") or "[]")
    except json.JSONDecodeError as e:
        raise click.ClickException(f"{path} bukan JSON yang valid: {e}")
    if not isinstance(data, list):
        raise click.ClickException(f"{path} harus berisi list task (JSON array).")
    return data


def save_tasks(path: Path, tasks: list[dict]) -> None:
    path.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


@click.group()
@click.option(
    "--data-file",
    type=click.Path(dir_okay=False, path_type=Path),
    default="data.json",
    envvar="TODO_DATA_FILE",
    show_default=True,
    help="Lokasi file penyimpanan task.",
)
@click.pass_context
def cli(ctx: click.Context, data_file: Path) -> None:
    """Aplikasi todo sederhana di command line."""
    ctx.obj = data_file


@cli.command()
@click.argument("title")
@click.pass_obj
def add(data_file: Path, title: str) -> None:
    """Tambah task baru."""
    title = title.strip()
    if not title:
        raise click.UsageError("Judul task tidak boleh kosong.")
    tasks = load_tasks(data_file)
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(data_file, tasks)
    click.echo(f"Ditambahkan #{new_id}: {title}")


@cli.command("list")
@click.pass_obj
def list_tasks(data_file: Path) -> None:
    """Tampilkan semua task."""
    tasks = load_tasks(data_file)
    if not tasks:
        click.echo("Belum ada task.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        click.echo(f"[{mark}] {t['id']}. {t['title']}")


@cli.command()
@click.argument("task_id", type=int)
@click.pass_obj
def done(data_file: Path, task_id: int) -> None:
    """Tandai task dengan ID tertentu sebagai selesai."""
    tasks = load_tasks(data_file)
    for t in tasks:
        if t["id"] == task_id:
            if t["done"]:
                click.echo(f"Task #{task_id} sudah selesai sebelumnya.")
                return
            t["done"] = True
            save_tasks(data_file, tasks)
            click.echo(f"Selesai #{task_id}: {t['title']}")
            return
    raise click.ClickException(f"Task #{task_id} tidak ditemukan.")
