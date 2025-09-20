import json
import os

from commands import (
    add_command,
    delete_command,
    list_command,
    mark_command,
    update_command,
)

test_data = [
    {"id": 0, "description": "buy broccoli", "status": "todo"},
    {"id": 1, "description": "buy broccoli", "status": "done"},
    {"id": 2, "description": "buy broccoli", "status": "in-progress"},
]


def test_add():
    file_name = "test_add.json"
    add_command.add(description="testing 0", file_name=file_name)
    add_command.add(description="testing 1", file_name=file_name)
    with open(file_name, "r") as file:
        data = json.load(file)

    os.remove(file_name)
    assert data[0]["id"] == 0
    assert data[1]["id"] == 1
    assert data[0]["description"] == "testing 0"
    assert data[0]["status"] == "todo"


def test_update():
    file_name = "test_update.json"
    with open(file_name, "w") as file:
        json.dump(test_data, file)

    update_command.update(
        id=0, description="buy broccoli and chili", file_name=file_name
    )
    with open(file_name, "r") as file:
        data = json.load(file)
    os.remove(file_name)

    assert data[0]["id"] == 0
    assert data[0]["description"] == "buy broccoli and chili"
    assert data[0]["status"] == "todo"


def test_delete():
    file_name = "delete_test.json"
    with open(file_name, "w") as file:
        json.dump(test_data, file)

    delete_command.delete(id=0, file_name=file_name)
    delete_command.delete(id=1, file_name=file_name)
    delete_command.delete(id=2, file_name=file_name)
    with open(file_name, "r") as file:
        data = json.load(file)

    os.remove(file_name)
    assert data == []


def test_list(capsys):
    file_name = "delete_test.json"
    with open(file_name, "w") as file:
        json.dump(test_data, file)

    list_command.list(filter="all", file_name=file_name)
    os.remove(file_name)
    captured = capsys.readouterr()
    expected = "id,description,status\n0,buy broccoli,todo\n1,buy broccoli,done\n2,buy broccoli,in-progress\n"
    assert captured.out == expected


def test_mark():
    file_name = "test_update.json"
    with open(file_name, "w") as file:
        json.dump(test_data, file)

    mark_command.mark(id=0, status="done", file_name=file_name)
    with open(file_name, "r") as file:
        data = json.load(file)
    os.remove(file_name)
    assert data[0]["status"] == "done"
