import geopandas as gpd
import pandas as pd

PD = pd.read_csv("stop2.csv")

PDList = PD["Agency Name"]
PD1 = PD[PD["Tier"]==1]
PD2 = PD[PD["Tier"]==2]
PDCO = bool(PD["Agency Name"].find('PD[Agency Name]', 'CO'))
print(PDCO["Agency Name"])



# location = "Beaverton, OR"
# query = f"'{location}'"

# # Download the shapefile using geopandas
# gdf = gpd.read_file(f"https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_place_500k.zip?#inside/{query}")
# # Save the downloaded shapefile to a local file
# gdf.to_file(f"{location}.shp")