import copy
import json

import pandas as pd
import requests

BASE_URL = "http://02049f7f-8dfe-409e-9112-30fbeed229cd.westus.azurecontainer.io/score" # Fill endpoint URL
BODY = {
    "data": [
    ]
}

def update_request(x):
    BODY['data'].append({
        'Date': x["Date"],
        'TZ': x["TZ"],
        'City': x["City"],
        'Code': x["Code"]
    })
    result = json.loads(json.loads(requests.post(url=BASE_URL, json=BODY).text))["forecast"][-1]
    return result


data = pd.read_csv(filepath_or_buffer='../datasets/energy-test.csv',
                   names=['Date', 'TZ', 'City', 'Code', 'Load'],
                   skiprows=1)
predicted = data.apply(lambda x: update_request(x), axis=1)
data2 = pd.concat([data, predicted], axis=1)
data2.to_csv(path_or_buf='../datasets/energy-pred.csv', index=False)
