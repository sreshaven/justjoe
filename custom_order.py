import csv
import difflib

# Function to find the best match from a list of strings
def find_best_match(input_str, str_list):
    closest_match = difflib.get_close_matches(input_str, str_list, n=1)
    return closest_match[0] if closest_match else None

# Load the CSV data into a dictionary (product as key, price as value)
csv_file = "filtered_output.csv"
product_prices = {}

with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            product_prices[row[0].strip().lower()] = float(row[1].strip())

# Person's input from app
person_input = ["latte", "vanilla syrup", "almond milk"]

print(product_prices)
# Calculate the total price based on the closest matches
total_price = 0.0

# loop through each item and find best match
for item in person_input:
    closest_product = find_best_match(item.lower(), product_prices.keys())
    if closest_product:
        total_price += product_prices[closest_product]


print(f"Total price for the order: ${total_price:.2f}")
