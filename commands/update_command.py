import json
import os


def update(id: int, description: str, file_name: str = "tasks.json"):
    if not os.path.exists(file_name):
        return 0
    with open(file_name, mode="r", encoding="utf-8") as file:
        data: list = json.load(file)
        found = False
        for i, d in enumerate(data):
            if d["id"] == id:
                found = True
                break
        if not found:
            return 1

        data[i]["description"] = description

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
