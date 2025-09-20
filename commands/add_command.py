import json
import os


def add(description: str, file_name: str = "tasks.json"):
    if not os.path.exists(file_name):
        with open(file_name, mode="w") as file:
            json.dump([], file)
    with open(file_name, mode="r", encoding="utf-8") as file:
        data = json.load(file)
        try:
            id: int = data[-1]["id"] + 1
        except:
            id: int = 0
        task = {"id": id, "description": description, "status": "todo"}

    with open(file_name, mode="w", encoding="utf-8") as file:
        data.append(task)
        json.dump(data, file, indent=4)
    print("Added", task)
