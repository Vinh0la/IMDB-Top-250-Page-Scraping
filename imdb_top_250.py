import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

root = "https://www.imdb.com/"
start_url = f"{root}/chart/top/?ref_=nv_mv_250"

path = r"C:\PythonFiles\chromedriver.exe"

driver = webdriver.Chrome(service=Service(path))
driver.get(start_url)

catalog = driver.find_elements(By.XPATH,"//ul[contains(@class,'ipc-metadata-list')]/li")

title = []
play_time = []
rating = []
year_release = []

for movie in catalog:
    title.append(movie.find_element(By.XPATH,'.//h3').text.lstrip("0123456789.").lstrip())
    play_time.append(movie.find_element(By.XPATH,".//div[contains(@class,'title-metadata')]/span[2]").text)
    rating.append(float(movie.find_element(By.XPATH,".//div[contains(@class,'cli-ratings')]/span").text[0:3]))
    year_release.append(movie.find_element(By.XPATH,".//div[contains(@class,'title-metadata')]/span[1]").text)

df = pd.DataFrame.from_dict({'Title':title,'Play time':play_time,'Rating':rating,'Release Year':year_release})
df.to_csv("Top 250.csv",index=False)

time.sleep(10)
driver.quit()
