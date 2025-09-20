# task-tracker-cli

This task tracker uses uv as package manager made for [roadmap task tracker](https://roadmap.sh/projects/task-tracker)

```
uv sync
```
## Add
```
uv run main.py add "test"
```
## Update
```
uv run main.py update 0 "test"
```
## Delete
```
uv run main.py delete 0
```
## Mark
done
```
uv run main.py mark done
```
todo
```
uv run main.py mark todo
```
in-progress
```
uv run main.py mark in-progress
```
## List
```
uv run main.py list
```
```
uv run main.py list all
```
```
uv run main.py list done
```
```
uv run main.py list todo
```
```
uv run main.py list in-progress
```
