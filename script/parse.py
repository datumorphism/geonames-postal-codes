import pandas as pd

all_countries_file = "~/Downloads/all_countries.txt"

df = pd.read_csv(all_countries_file, sep="\t")

df_pc = df.groupby(["country_code", "postal_code"]).agg(
    {
        "latitude": "mean",
        "longitude": "mean"
    }
).reset_index()

df_pc.to_csv("postal_codes_and_coordinates.csv", index=False)
df_pc.to_json("postal_codes_and_coordinates.json", orient="records")