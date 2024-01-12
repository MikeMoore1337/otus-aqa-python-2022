import json
import csv
from csv import DictReader

data = []

with open("users.json", "r") as json_file:
    users = json.load(json_file)
    for user in users:
        data.append(
            {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
        )

with open("books.csv", "r") as csv_file:
    books = csv.DictReader(csv_file)
    i = 0
    for book in books:
        data[i % len(data)]["books"].append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"]
            }
        )
        i += 1

with open("result.json", "w") as out_file:
    json.dump(data, out_file, indent=4)
