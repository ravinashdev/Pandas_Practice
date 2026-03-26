from operator import index

import pandas as pd
from pandas import DataFrame
# Import CSV
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_Data.csv")
# Convert to an iterable list to see available columns
squirrel_data_columns_list = squirrel_data.columns.tolist()
# Target specific column "Primary Fur Colors"
primary_fur_color_column = squirrel_data["Primary Fur Color"]
# Convert unique values in the column to an iterable list
primary_fur_colors = squirrel_data["Primary Fur Color"].unique().tolist()[1:]
# Count each value based on the unique color
primary_fur_color_count = squirrel_data["Primary Fur Color"].value_counts()
# Create a new DataFrame/Series and export to CSV
print(type(primary_fur_color_count))
print(primary_fur_color_count)
primary_fur_color_count_dataframe = pd.DataFrame(primary_fur_color_count)
print(primary_fur_color_count_dataframe)
primary_fur_color_count_dataframe.to_csv("primary_fur_color_count.csv")