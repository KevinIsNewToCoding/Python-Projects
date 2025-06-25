"""Basic pandas operations demonstration.

This script loads a CSV file and shows how to inspect and select data.
"""

import pandas as pd

# Load the sales data
sales_path = "data/sales.csv"
df = pd.read_csv(sales_path)

# View the first few rows
print("=== HEAD ===")
print(df.head())

# Show DataFrame information
print("\n=== INFO ===")
df.info()

# Statistical summary of numeric columns
print("\n=== DESCRIBE ===")
print(df.describe())

# Select a single column
regions = df["Region"]
print("\nRegions column:")
print(regions.head())

# Select multiple columns
products_quantities = df[["Product", "Quantity"]]
print("\nProduct and Quantity columns:")
print(products_quantities.head())

# Save DataFrame to a new CSV
output_path = "data/output_basic.csv"
df.to_csv(output_path, index=False)
print(f"\nData saved to {output_path}")
