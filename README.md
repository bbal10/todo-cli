# todo-cli

Aplikasi todo sederhana di command line, dibuat dengan Python dan [Click](https://click.palletsprojects.com/). Task disimpan di file JSON lokal.

## Kebutuhan

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Instalasi

```sh
git clone <repo-url>
cd todo-cli
uv sync
```

Perintah ini membuat `.venv` dan memasang proyek (mode editable) beserta dependensinya.

## Penggunaan

### Tambah task

```sh
uv run todo add "Beli susu"
```

```
Ditambahkan #1: Beli susu
```

### Lihat semua task

```sh
uv run todo list
```

```
[ ] 1. Beli susu
[ ] 2. Kirim laporan mingguan
[ ] 3. Olahraga pagi
```

### Tandai task selesai

```sh
uv run todo done 2
```

```
Selesai #2: Kirim laporan mingguan
```

```sh
uv run todo list
```

```
[ ] 1. Beli susu
[x] 2. Kirim laporan mingguan
[ ] 3. Olahraga pagi
```

### Kasus lain

Menandai task yang sudah selesai:

```
$ uv run todo done 2
Task #2 sudah selesai sebelumnya.
```

ID yang tidak ada (exit code 1):

```
$ uv run todo done 99
Error: Task #99 tidak ditemukan.
```

Belum ada task sama sekali:

```
$ uv run todo list
Belum ada task.
```

Jalankan `uv run todo --help` atau `uv run todo <perintah> --help` untuk bantuan lengkap.

## File data (`data.json`)

Task disimpan di `data.json` pada **direktori tempat kamu menjalankan perintah**.

- **Tidak perlu membuat file sendiri.** Kalau `data.json` belum ada, file dibuat otomatis (berisi `[]`) saat perintah pertama dijalankan.
- Kalau mau menyiapkan data awal, buat `data.json` berisi array task dengan format berikut:

  ```json
  [
    { "id": 1, "title": "Beli susu", "done": false },
    { "id": 2, "title": "Kirim laporan mingguan", "done": true }
  ]
  ```

- ID task baru adalah ID terbesar yang ada + 1.
- Jika isi file bukan JSON yang valid atau bukan array, perintah berhenti dengan pesan error dan file tidak diubah.

Untuk memakai lokasi lain, pakai opsi `--data-file` atau environment variable `TODO_DATA_FILE`:

```sh
uv run todo --data-file ~/todo.json list
TODO_DATA_FILE=~/todo.json uv run todo add "Bayar listrik"
```

> Tambahkan `data.json` ke `.gitignore` kalau tidak ingin ikut ter-commit.

## Struktur proyek

```
todo-cli/
├── pyproject.toml        # metadata proyek dan entry point `todo`
├── src/
│   └── todo_cli/
│       ├── __init__.py
│       └── main.py       # definisi perintah Click (`cli`, `add`, `list`, `done`)
└── uv.lock
```

Console script `todo` dideklarasikan di `pyproject.toml`:

```toml
[project.scripts]
todo = "todo_cli.main:cli"
```

## Pengembangan

Setelah mengubah `pyproject.toml` (misalnya entry point), jalankan ulang `uv sync` agar script `todo` dibuat ulang.
