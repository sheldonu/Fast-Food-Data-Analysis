import pandas as pd

# Read the data from the csv file

fast_food_data = pd.read_csv('FastFoodNutritionMenuV2.csv')

# Display all the data in table like terms

print(fast_food_data.describe)


### Try to find out the food item that gives you the best ratio of calorie/protein. 


# Calculate protein-to-calorie ratio for each item

fast_food_data['Protein (g)'] = pd.to_numeric(fast_food_data['Protein (g)'], errors='coerce')
fast_food_data['Calories'] = pd.to_numeric(fast_food_data['Calories'], errors='coerce')

# Calculate protein-to-calorie ratio for each item
fast_food_data['Protein_to_Calorie_Ratio'] = fast_food_data['Protein (g)'] / fast_food_data['Calories']

# Find the item with the highest protein-to-calorie ratio
best_ratio_item = fast_food_data.loc[fast_food_data['Protein_to_Calorie_Ratio'].idxmax()]

print("Item with the best protein-to-calorie ratio:")
print(best_ratio_item[['Item', 'Calories', 'Protein (g)', 'Protein_to_Calorie_Ratio']])

# This example above doesn't seem like it is right, I looked into the dataset where the Premium Hot Coffee is found, and I saw that
# all the data from Taco Bell is one column behind for all the values, so it doesn't give the right value/answer.


# Same code but exclude Taco Bell values


fast_food_data['Protein (g)'] = pd.to_numeric(fast_food_data['Protein (g)'], errors='coerce')
fast_food_data['Calories'] = pd.to_numeric(fast_food_data['Calories'], errors='coerce')

# Exclude rows with company name 'Taco Bell'
filtered_data = fast_food_data[fast_food_data['Company'] != 'Taco Bell']

# Calculate protein-to-calorie ratio for each item
filtered_data['Protein_to_Calorie_Ratio'] = filtered_data['Protein (g)'] / filtered_data['Calories']

# Find the item with the best protein-to-calorie ratio in the filtered data
best_ratio_item = filtered_data.loc[filtered_data['Protein_to_Calorie_Ratio'].idxmax()]

print("Item with the best protein-to-calorie ratio (excluding Taco Bell):")
print(best_ratio_item[['Item', 'Calories', 'Protein (g)', 'Protein_to_Calorie_Ratio']])