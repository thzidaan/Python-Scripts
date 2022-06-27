from selenium import webdriver
from selenium.webdriver.chrome.options import Options #Required for headless-mode 
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
string_time = now.strftime('%d%m%y')



news_website = 'https://www.thesun.co.uk/sport/football/'
driver_path = '/Users/zidaan/Documents/ChromeDriver/chromedriver'

# headless-mode --> The program won't open the browser and everything will happen in the background
options = Options()
options.headless = True


service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service,options=options) # Add options for headless-mode
driver.get(news_website)

#find_element only gives you the first element
#driver.find_element(by='xpath',value='//div[@class="teaser__copy-container"]')

containers = driver.find_elements(by='xpath',value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []


for container in containers:
    
    title = container.find_element(by='xpath',value='./a/h2').text 
    subtitle = container.find_element(by='xpath',value='./a/p').text
    link = container.find_element(by='xpath',value='./a').get_attribute('href')
    
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'Titles':titles, 'Sub-Titles':subtitles, 'Link': links}
df_headlines = pd.DataFrame(my_dict)

filename = f'theSun-headlines--{string_time}.csv' 
final_path = os.path.join(app_path,filename)


df_headlines.to_csv(final_path)

#Quit your driver
driver.quit()