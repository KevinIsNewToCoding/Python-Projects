"""Filtering, sorting, and adding columns with pandas."""

import pandas as pd

sales_path = "data/sales.csv"
df = pd.read_csv(sales_path)

# Filter rows where quantity is greater than 5
filtered = df[df["Quantity"] > 5]
print("=== Quantity > 5 ===")
print(filtered)

# Sort by price descending
sorted_df = df.sort_values(by="Price", ascending=False)
print("\n=== Sorted by Price (desc) ===")
print(sorted_df)

# Add a new column for total sale value
# (quantity multiplied by price)
df["Total"] = df["Quantity"] * df["Price"]
print("\n=== With Total column ===")
print(df)

# Save the updated DataFrame
output_path = "data/output_filtering_sorting.csv"
df.to_csv(output_path, index=False)
print(f"\nData saved to {output_path}")
