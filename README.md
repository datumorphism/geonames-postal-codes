# geonames-postal-codes-geocoordinates

The data is from geonames.

Several columns have been dropped to simplify the dataset.

## How to regenerate the data

1. Download the `allCountries.zip` from https://download.geonames.org/export/zip/
2. Unzip the data and place the file `allCountries.txt` into the folder `raw`.
3. Transform the data using the `python script/parse.py`.
4. Validate the results using `python test/quality.py`

## Missing Values in allCountries.zip

![](assets/all_countries_missing_values.png)
