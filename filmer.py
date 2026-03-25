import json

file = "movies.json"

with open(file, "r", encoding="utf-8") as f:
    movies = json.load(f)

print("Alle filmer:", movies)

action = input("add / del: ")

if action == "add":
    name = input("Film navn: ")
    movies.append(name)

elif action == "del":
    name = input("Delete film: ")
    if name in movies:
        movies.remove(name)

with open(file, "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False)

print("REady!")