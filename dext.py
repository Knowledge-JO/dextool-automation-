from tbselenium.tbdriver import TorBrowserDriver
import time
import random
with TorBrowserDriver("./tor-browser_en-US") as driver:
    SLEEP_TIME = 30 #random.randint(5, 10)
    SLEEP_TIME_1 = random.randint(4, 8)
    SLEEP_TIME_2 = random.randint(2, 5)
    tokenurl = "Dextool Link"
    while True:
        driver.get(tokenurl)
        time.sleep(SLEEP_TIME)
        print("Running favourite click")
        #fav button
        try:
            favbtn = driver.find_element_by_xpath('/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div/div[2]/div[2]/ul/li[1]/button[3]')
            favbtn.click()
        except:
            favbtn = driver.find_element_by_xpath('/html/body/app-root/div[2]/div/main/app-exchange/div/app-pairexplorer/app-layout/div/div[2]/div[2]/div[2]/ul/li[1]/button[3]')
            favbtn.click()
        time.sleep(SLEEP_TIME_1)
