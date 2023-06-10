import csv
import json


def convert_to_json(csvFilePath, jsonFilePath):

    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['UserID']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


convert_to_json("virtual_reality_exp.csv", "virtual_reality_exp.json")
