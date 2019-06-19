# Importing necessary modules
from urllib.request import Request, urlopen 
import urllib,json                            
import pandas as pd                           
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

ContestID = "JUNE19A"

# get the max page_number 
driver = webdriver.Chrome("C:/Users/Shrikha/Desktop/chromedriver_win32/chromedriver.exe") # Take the absolute path for Chrome Driver 
path1 = "https://www.codechef.com/rankings/"+ContestID
driver.get(path1)
wait = WebDriverWait(driver,600)
page_numbers = driver.find_elements_by_xpath('//*[@id="ember392"]/div[2]/div[3]/ul/li')
pagef = [x.text for x in page_numbers]
last_pagen = int(pagef[-1])
driver.close()

# Declaring necessary variables
pages = [str(i) for i in range(1,last_pagen+1)]


# declaring the lists to store data in
rank = []
userHandle = []
name = []


for page in pages:
    # make a request
    path = 'https://www.codechef.com/api/rankings/'+ContestID+'?sortBy=score&order=desc&page='+page+'&itemsPerPage=100'
    req = Request(path , headers = {'User-Agent':'Mozilla/5.0'})
    webpage = urlopen(req)
    
    # Parse json data
    obj = json.load(webpage)
    i = obj['list']

    # Extracting data
    for j in range(len(i)):
        rank.append(i[j]['rank'])
        userHandle.append(i[j]['user_handle'])
        name.append(i[j]['name'])

# creating a Dataframe
df = pd.DataFrame({'user_handle':userHandle,'name':name},index = rank).sort_index()

# Saving into a csv format
df.to_csv('C:/users/Shrikha/Desktop/ContestRanking.csv')  
