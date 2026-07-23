# 📂 File Handling

## Reading a File

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

## Writing to a File

```python
with open("output.txt", "w") as file:
    file.write("Hello, Cybersecurity!")
```

---

## Appending

```python
with open("log.txt", "a") as file:
    file.write("New Log Entry\n")
```

---

## CSV Example

```python
import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## JSON Example

```python
import json

data = {"name": "Aditysinh"}

print(json.dumps(data, indent=4))
```

---

# Cybersecurity Use Cases

- Log parsing
- Report generation
- IOC storage
- Configuration management
