import pandas as pd
import csv
import json


def clean_csv(csv_file):

    df = pd.read_csv(csv_file)
    df = df.drop(columns=['Gender'])
    df = df.rename(columns={"UserID": "pk", "Age": "user_age", "VRHeadset": "headset_type", "Duration": "duration_of_use",
                            "MotionSickness": "motion_sickness", "ImmersionLevel": "immersion_level"})
    df['user_age'] = df['user_age'].astype(int)
    df['duration_of_use'] = df['duration_of_use'].astype(float)
    df['motion_sickness'] = df['motion_sickness'].astype(int)
    df['immersion_level'] = df['immersion_level'].astype(int)
    df.to_csv('vr_experience_cleaned.csv', encoding='utf-8', index=False)


# clean_csv("virtual_reality_exp.csv")

# convert to json to add file to django fixtures for preloading/seeding data
def convert_to_json(csv_file, jsonFilePath):
    data = []
    with open(csv_file, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            rows['pk'] = int(rows['pk'])
            rows['user_age'] = int(rows['user_age'])
            rows['duration_of_use'] = float(rows['duration_of_use'])
            rows['motion_sickness'] = int(rows['motion_sickness'])
            rows['immersion_level'] = int(rows['immersion_level'])

            fields = {
                'user_age': rows['user_age'],
                'headset_type': rows['headset_type'],
                'duration_of_use': rows['duration_of_use'],
                'motion_sickness': rows['motion_sickness'],
                'immersion_level': rows['immersion_level']
            }
            new_key = {"model": "vr_exp.Experience",
                       "pk": rows['pk'], "fields": fields}
            data.append(new_key)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


convert_to_json("vr_experience_cleaned.csv", "virtual_reality_exp.json")
