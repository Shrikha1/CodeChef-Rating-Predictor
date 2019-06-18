# Importing necessary modules
from urllib.request import Request, urlopen   # to access data from the url 
import urllib,json                            # to parse json data
import pandas as pd                           # to organise data in csv format

ContestID = 'JUNE19A'
#path = 'https://www.codechef.com/api/rankings/'+ContestID
path = 'https://www.codechef.com/api/rankings/'+ContestID+'?sortBy=score&order=desc&page=1&itemsPerPage=100'
req = Request(path , headers = {'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req)
obj = json.load(webpage)

rank = []
userHandle = []
name = []
i = obj['list']

# Extracting data
for j in range(len(i)):
    rank.append(i[j]['rank'])
    userHandle.append(i[j]['user_handle'])
    name.append(i[j]['name'])

# creating a Dataframe
df = pd.DataFrame({'user_handle':userHandle,'name':name},index = rank).sort_index()

# Saving into a csv format
df.to_csv('ContestRanking.csv')  

