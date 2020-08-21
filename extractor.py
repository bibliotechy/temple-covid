from bson import dumps as bdumps
import datetime
from json import dumps as jdumps
import pandas as pd
import plyvel
import requests



doc = requests.get(
    "https://www.temple.edu/life-temple/health-wellness/coronavirus-planning-safe-return/university-communication/active-covid-19-cases-temple-university"
    ).text

# reads all of the tables in the html into a dataframe
# since there is only one, grab the first
original_df = pd.read_html(doc)[0]

# The dataframe treats the first column of the table, as a data column
# but it is actually the labels of student, staff, and total
# so we're going to set that column as the index.
# Next, we tanspose the index and columns because I was more interested in 
# grouping groups (Students, staff) than I was about grouping locations

df = ( 
    original_df
    .set_index(original_df.columns[0])
    .transpose()
    .to_dict()
)

now = datetime.datetime.now().isoformat()

output_dict = {
    "timestamp": now,
    "data": df
}

db = plyvel.DB("./data", create_if_missing=True)
db.put(now.encode('utf-8'), bdumps(df))

print(jdumps(output_dict))