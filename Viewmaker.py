from selenium import webdriver
import time
no_of_driver=int(input("Enter no of drivers or Windows : "))
url= input("Enter url : ")
time_to_refresh=int(input("Enter refresh rate in second : "))

drivers=[]
for i in range(no_of_driver):
    drivers.append(webdriver.Chrome("chromedriver.exe"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()
