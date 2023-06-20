import pandas as pd
import pycountry
import numpy as np

data = pd.read_csv("docs/climate_change_data.csv")

# Convert the 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Filter the dataset for the year 2021
filtered_data = data[data['Date'].dt.year == 2021]

# Group by country and take the mean of all data from 2021
averages_climate_df = filtered_data.groupby('Country').mean(True).reset_index()


# averages_climate_df.to_csv("climate_data_2021.csv")

hdi_data = pd.read_csv("docs/HumanDevelopmentData.csv")

def do_fuzzy_search(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
        return result[0].alpha_3
    except:
        return "UNKNOWN"

aggregated_dataset = pd.merge(averages_climate_df, hdi_data, on="Country")
aggregated_dataset["ISO-code"] = aggregated_dataset["Country"].apply(lambda country: do_fuzzy_search(country))
aggregated_dataset.to_csv("aggregated_dataset.csv")
