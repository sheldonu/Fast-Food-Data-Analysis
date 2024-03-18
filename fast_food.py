import pandas as pd

fast_food_data = pd.read_csv('FastFoodNutritionMenuV2.csv')

print(fast_food_data.drop(columns=['Company', 'Item']))