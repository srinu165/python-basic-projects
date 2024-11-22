from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
t=str(input("enter song name:"))
if(t=="prabhas"):
    driver = webdriver.Firefox()
    query = "youtube"
    driver.get(f"https://www.youtube.com/watch?v=TPYg7NBo4yY")
    ele = driver.find_element(By.class_Name,"sg-col-inner")
    print(ele.text)
    driver.close()
elif(t=="alluarjun"):
    driver = webdriver.Firefox()
    query = "youtube"
    driver.get(f"https://www.youtube.com/watch?v=txHO7PLGE3o")
    ele = driver.find_element(By.class_Name,"sg-col-inner")
    print(ele.text)
    driver.close()
elif(t=="open facebook"):
    driver = webdriver.Firefox()
    query = "facebook"
    driver.get(f"https://www.facebook.com/")
    ele = driver.find_element(By.class_Name,"sg-col-inner")
    print(ele.text)
    driver.close()
elif(t=="open github"):
    driver = webdriver.Firefox()
    query = "github"
    driver.get(f"https://github.com/")
    ele = driver.find_element(By.class_Name,"sg-col-inner")
    print(ele.text)
    driver.close()
else:
    print("unknown error occured") 
