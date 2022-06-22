from typing import List
import pandas as pd
import random

from app.exceptions import ParkNotFoundExcpetion
from app.constants import resources_dir

PARK_TABLE_FILEPATH = 'nature_parks_table_features_20220622.csv'

df_parks = pd.read_csv(resources_dir.joinpath(PARK_TABLE_FILEPATH))

def find_park_by_desc(park_state: str, park_desc: List[str]):
    mask = (df_parks["State"] == park_state) & \
        (pd.DataFrame([df_parks[feature] for feature in park_desc]).all())
    candidates = list(df_parks["Name"][mask])

    if len(candidates) == 0:
        raise ParkNotFoundExcpetion()

    return random.choice(candidates)

def get_park_year_area_summary(park_name: str):
    if park_name not in df_parks["Name"].values:
        raise ParkNotFoundExcpetion()
    return tuple(df_parks[["Year", "Area (km²)", "Summary"]][df_parks["Name"] == park_name].iloc[0])