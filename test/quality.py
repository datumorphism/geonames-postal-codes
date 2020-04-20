import pandas as pd

df_pc = pd.read_csv("dataset/postal_codes_and_coordinates.csv")

df_pc_dup_counts = df_pc.groupby(["country_code", "postal_code"]).agg(
    {
        "latitude": "count",
        "longitude": "count"
    }
).reset_index()


print(f"Total rows: {len(df_pc)}")
print(df_pc_dup_counts.sort_values(by=["latitude", "longitude"], ascending=False).head())

