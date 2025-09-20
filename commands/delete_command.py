import json


def delete(id: int, file_name: str = "tasks.json"):
    with open(file_name, "r") as file:
        data: list = json.load(file)
        found = False
        ind = None
        for i, d in enumerate(data):
            if d["id"] == id:
                ind = i
                break
        del data[ind]
    with open(file_name, "w") as file:
        json.dump(data, file)
