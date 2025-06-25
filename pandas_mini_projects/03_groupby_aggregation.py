"""GroupBy and aggregation examples with pandas."""

import pandas as pd

sales_path = "data/sales.csv"
df = pd.read_csv(sales_path)

# Total quantity sold by region
region_totals = df.groupby("Region")["Quantity"].sum()
print("=== Total Quantity by Region ===")
print(region_totals)

# Average price by product
product_price_mean = df.groupby("Product")["Price"].mean()
print("\n=== Average Price by Product ===")
print(product_price_mean)

# Multiple aggregation operations
agg_df = df.groupby("Product").agg({"Quantity": "sum", "Price": "mean"})
print("\n=== Aggregated Data ===")
print(agg_df)

# Save aggregated result
agg_output_path = "data/output_groupby.csv"
agg_df.to_csv(agg_output_path)
print(f"\nAggregated data saved to {agg_output_path}")
