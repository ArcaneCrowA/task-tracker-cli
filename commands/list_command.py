import json


def list(filter: str, file_name: str = "tasks.json"):
    with open(file_name, "r") as file:
        data = json.load(file)
    results = [["id", "description", "status"]]
    if filter == "all":
        for d in data:
            results.append([str(d["id"]), d["description"], d["status"]])
    elif filter == "todo":
        for d in data:
            if d.get("status") == "todo":
                results.append([str(d["id"]), d["description"], d["status"]])
    elif filter == "done":
        for d in data:
            if d.get("status") == "done":
                results.append([str(d["id"]), d["description"], d["status"]])
    elif filter == "in-progress":
        for d in data:
            if d.get("status") == "in-progress":
                results.append([str(d["id"]), d["description"], d["status"]])
    else:
        print("not a valid option")
        return
    for res in results:
        print(",".join(res))
