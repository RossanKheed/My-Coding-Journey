# Simple matching algorithm
students = [
    {"name": "You", "country": "Tanzania", "field": "CS"},
    {"name": "Friend", "country": "Kenya", "field": "Engineering"},
]

scholarships = [
    {"name": "Google Tanzania", "country": "Tanzania"},
    {"name": "World Bank Africa", "country": "Any"},
]

for student in students:
    print(f"\n{student['name']}'s matches:")
    for scholarship in scholarships:
        if scholarship["country"] == student["country"] or scholarship["country"] == "Any":
            print(f"  ✅ {scholarship['name']}")