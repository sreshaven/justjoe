##input image and convert it to text
import csv
import re
import pytesseract
from PIL import Image

# Open the image file
image = Image.open('menu3.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)

# print("start of text", text, "end of text")

## now read all that text and split it into three columns (product, small price, large price)
data = text

# Split the data into lines
lines = data.split('\n')
print(lines)
# Initialize lists to store product and price data
products = []
small_prices = []
large_prices = []

# Iterate through the lines and extract product and price information
for line in lines:
    # see if there's a number in the line
    match = re.search(r'\d', line)
    # Split lines with ":" to extract prices
    if '$' in line:
        product, price = [item.strip() for item in line.split("$", 1)]
        if '/' in price:
            small_price, large_price = [item.strip() for item in price.split("/")]
            small_prices.append(small_price)
            large_prices.append(large_price)
        else:
            small_prices.append(price)
            large_prices.append('')
        products.append(product)
    # Lines without ":" may contain additional product or irrelevant information
    elif match:
        index = match.start()
        products.append(line[:index].strip())
        small_prices.append(line[index:].strip())
        large_prices.append('')



# Create a list of rows to write to the CSV file
rows = list(zip(products, small_prices, large_prices))

# Specify the name of the CSV file
csv_file = "output.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Small Size Price', 'Large Size Price'])
    writer.writerows(rows)

print(f"Data has been written to '{csv_file}'.")
