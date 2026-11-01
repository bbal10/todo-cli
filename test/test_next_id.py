from todo_cli.main import next_id

def test_next_id_empty_list():
    assert next_id([]) == 1

def test_next_id_max_plus_one():
    tasks = [{"id": 1, "title": "Task 1", "done": False}, {"id": 2, "title": "Task 2", "done": True}]
    assert next_id(tasks) == 3