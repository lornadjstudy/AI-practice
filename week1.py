import json

employees = [
    {"name": "Ana", "department": "HR", "status": "active"},
    {"name": "Petra", "department": "TSG", "status": "active"},
    {"name": "Liza", "department": "ADM", "status": "inactive"},
    {"name": "Ara", "department": "TSG", "status": "active"},
    {"name": "Ada", "department": "ADM", "status": "active"}
]

# Save to a file
with open("employees.json", "w") as f:
    json.dump(employees, f, indent=2)

# Read it back
with open("employees.json", "r") as f:
    loaded = json.load(f)

print("All ADM:")
for person in loaded:
    if person["department"] == "ADM":
        print(person["name"])

print("Active ADM only:")
for person in loaded:
    if person["department"] == "ADM" and person["status"] == "active":
        print(person["name"])
