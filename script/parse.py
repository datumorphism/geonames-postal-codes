import pandas as pd

all_countries_file = "raw/allCountries.txt"

columns ="""country code      : iso country code, 2 characters
postal code       : varchar(20)
place name        : varchar(180)
admin name1       : 1. order subdivision (state) varchar(100)
admin code1       : 1. order subdivision (state) varchar(20)
admin name2       : 2. order subdivision (county/province) varchar(100)
admin code2       : 2. order subdivision (county/province) varchar(20)
admin name3       : 3. order subdivision (community) varchar(100)
admin code3       : 3. order subdivision (community) varchar(20)
latitude          : estimated latitude (wgs84)
longitude         : estimated longitude (wgs84)
accuracy          : accuracy of lat/lng from 1=estimated, 4=geonameid, 6=centroid of addresses or shape"""

columns = ["_".join(i.split(":")[0].strip().split(" ")) for i in columns.split("\n")]
col_types = {
    "country_code": str,
    "postal_code": str,
    "latitude": float,
    "longitude": float
}

df = pd.read_csv(all_countries_file, sep="\t", names=columns, dtype=col_types)

for col in ["country_code", "postal_code"]:
    df[col] = df[col].apply(lambda x: x.strip())
    df[col] = df[col].apply(lambda x: x.strip())

df = df[["country_code", "postal_code", "latitude", "longitude"]]

df["longitude"] = df.longitude.astype(float)
df["latitude"] = df.latitude.astype(float)

print(df.head())

df_pc = df.groupby(["country_code", "postal_code"]).agg(
    {
        "latitude": "mean",
        "longitude": "mean"
    }
).reset_index()


df_pc_dup_counts = df_pc.groupby(["country_code", "postal_code"]).agg(
    {
        "latitude": "count",
        "longitude": "count"
    }
).reset_index()

print(df_pc_dup_counts.sort_values(by=["latitude", "longitude"], ascending=False).head())


df_pc.to_csv("dataset/postal_codes_and_coordinates.csv", index=False)
df_pc.to_json("dataset/postal_codes_and_coordinates.json", orient="records")