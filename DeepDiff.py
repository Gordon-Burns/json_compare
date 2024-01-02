import json
from deepdiff import DeepDiff

#Opening JSON file
f = open('JSON_1.json')
# returns JSON object as a dictionary
data = json.load(f)

# Opening JSON file
f = open('JSON_2.json')
# returns JSON object as
# a dictionary
data_1 = json.load(f)

ddiff = DeepDiff(data,data_1)
results_dict = {}

for index, (key, value) in enumerate(ddiff.items()):

    if isinstance(value, dict):
        # If the value is a dictionary, iterate through its items
        for k, v in value.items():
            position_number = int(k.split('[')[1].split(']')[0])
            ID = data_1[position_number]["ID"]
            name = data_1[position_number]["Name"]

            result_key = f"{key} - {name}"
            results_dict[result_key] = {
                "ID": ID,
                "Name": name,
                "Values": v
            }

            # Write the results dictionary to a new JSON file
            with open('results.json', 'w') as result_file:
                json.dump(results_dict, result_file, indent=2)

            print("Results have been written to results.json.")





