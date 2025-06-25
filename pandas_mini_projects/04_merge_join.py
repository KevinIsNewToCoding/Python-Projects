"""Examples of merging and joining DataFrames with pandas."""

import pandas as pd

customers_path = "data/customers.csv"
orders_path = "data/orders.csv"

customers = pd.read_csv(customers_path)
orders = pd.read_csv(orders_path)

# Merge orders with customer info
merged = pd.merge(orders, customers, on="customer_id", how="left")
print("=== Merged Data ===")
print(merged)

# Another join example: inner join on region
# For demonstration, merge the merged data with sales on product and region
sales = pd.read_csv("data/sales.csv")
join_example = pd.merge(merged, sales, on=["product", "Region"], how="inner")
print("\n=== Joined with Sales ===")
print(join_example)

# Save results
merged.to_csv("data/output_merged.csv", index=False)
join_example.to_csv("data/output_join_example.csv", index=False)
print("\nOutputs saved to data/ directory")
