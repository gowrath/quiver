from bs4 import BeautifulSoup
from numpy import datetime_as_string
import requests
import pandas as pd
import json
import pathlib
from datetime import datetime


var = input("Enter a ticker (four letter symbol):  ")

now = datetime.now()


url = "https://api.quiverquant.com/beta/historical/congresstrading/"+str(var)
headers = {'accept': 'application/json',
'X-CSRFToken': 'TyTJwjuEC7VV7mOqZ622haRaaUr0x0Ng4nrwSRFKQs7vdoBcJlK9qjAS69ghzhFu',
'Authorization': 'Token 51fe4d1e20622e27494e727f7df3662ea3dcc65e'
}
r = requests.get(url, headers=headers)

df = pd.json_normalize(r.json())


file_name = now.strftime("%Y%m%d-%H%M%S") + '.csv'


df.to_csv(file_name, index = False)

