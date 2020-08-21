import datetime
import json
import pandas as pd
import requests



doc = requests.get(
    "https://www.temple.edu/life-temple/health-wellness/coronavirus-planning-safe-return/university-communication/active-covid-19-cases-temple-university"
    ).text

# reads all of the tables in the html into a dataframe
# since there is only one, grab the first
df = pd.read_html(doc)[0]

# The dataframe treats the first column of the table, as a data column
# but it is actually the labels of student, staff, and total
# so we're pop
ddf = df.to_dict()
groups = ddf.pop('Unnamed: 0')


output_dict = {
    "timestamp": datetime.datetime.now().isoformat(),
    "data": {}
}

for index, group in groups.items():
    output_dict["data"][group] = { k:v[index] for k,v in ddf.items()}

print(json.dumps(output_dict))