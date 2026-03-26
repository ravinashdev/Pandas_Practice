# IMPORTS
import csv
import itertools
import pandas as pd
from json import loads, dumps
import json

# with open("Weather_Data.csv") as data:
#     # Creates an iterable object
#     data = csv.reader(data)
#     days_of_the_week = []
#     temperature = []
#     conditions = []
#     # Using itertools to slice an iterable object since it has no index to remove csv column labels
#     for row in itertools.islice(data, 1, None):
#         days_of_the_week.append(row[0])
#         temperature.append(int(row[1]))
#         conditions.append(row[2])
#     print(days_of_the_week)
#     print(temperature)
#     print(conditions)

data = pd.read_csv("Weather_Data.csv")
# Print a table
# Data type of data is a DataFrame
print(data)
print(type(data))
# Print a column
# Data type of data["Temo"] is a Series = List
print(data["Temp"])
print(type(data["Temp"]))

# PANDAS to JSON
df = pd.DataFrame(
   [["a", "b"], ["c", "d"]],
    index=["row 1", "row 2"],
   columns=["col 1", "col 2"],
)
result = df.to_json(orient="split")
parsed = loads(result)
dumps(parsed, indent=4)
print(json.dumps(parsed, indent=4))

# Dataframes
print(data.head())
data_dict_records = data.to_dict("records")
data_dict_tight = data.to_dict("tight")
print(data_dict_records)
print(data_dict_tight)

# Series
temperature_list = data["Temp"].tolist()
average_temperature = data["Temp"].mean()
average_temperature_1 = data.Temp.mean()
maximum_temperature = data["Temp"].max()
maximum_temperature_1 = data.Temp.max()
print(f"Average Temperature: {average_temperature}")
print(f"Maximum Temperature: {maximum_temperature}")
print(f"Average Temperature 1: {average_temperature_1}")
print(f"Maximum Temperature 1: {maximum_temperature_1}")

# Get data in a row
monday_data = data[data.Day == "Monday"]
max_temp_row = data[data["Temp"] == data["Temp"].max()]
max_temperature_in_max_row_celsius = max_temp_row["Temp"].iloc[0]
max_temperature_in_max_row_fahrenheit = (max_temperature_in_max_row_celsius*1.8)+32
print(monday_data)
print(max_temp_row)
print(max_temperature_in_max_row_celsius)
print(max_temperature_in_max_row_fahrenheit)

# Create a DataFrame and export to CSV
data_dict = {
    "students":["Ryan","Aleks","Brandon","Danial"],
    "scores":[100,99,98,97]
}
new_data_frame = pd.DataFrame(data_dict)
print(new_data_frame)
new_data_frame.to_csv("student_scores.csv")