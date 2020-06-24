from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from soup import scrape
actual_path = "C:/Users/Owner/Desktop/chromedriver"
class Driver():
    def __init__(self):
        self.options = Options()
        
        
        self.driver = webdriver.Chrome(executable_path=actual_path , options=self.options)
    def auto(self):
        xpath = self.driver.find_element_by_xpath
        self.driver.get("https://www.msn.com")
        sleep(1)
        outlook_btn = xpath('//*[@id="main"]/div[1]/div[1]/div/ul/li[1]/a')
        outlook_btn.click()
        sleep(2)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        try:
            
            login_btn = xpath('//*[@id="office-Hero5050-e0h0pts"]/section/div/div[1]/div/div/div/div/div[2]/a')
            login_btn.click()
            sleep(3)
            print(self.driver.window_handles)
        except:
            
            login_btn = xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a')
            login_btn.click()
        sleep(2)
        email = xpath('//*[@id="i0116"]')
        email.send_keys('chadwilles@msn.com')
        submit = xpath('//*[@id="idSIButton9"]')
        submit.click()
        sleep(1)
        password = xpath('//*[@id="i0118"]')
        password.click()
        password.send_keys('')
        submit_btn2 = xpath('//*[@id="idSIButton9"]')
        submit_btn2.click()
        sleep(2)
        try:
            alside_btn = xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[10]/div')
            alside_btn.click()
        except:
            alside_btn = xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[10]/div')
            alside_btn.click()
        sleep(5)
        try:
            items = self.driver.find_elements_by_tag_name("div")
            for item in items:
                if str(item.text) == "Larry Thatcher":
                    item.click()
                    scrape(self.driver.page_source)
                    
                    alside_btn.click()
                    sleep(1)
        except Exception as e:
            try:
                sleep(5)
                print(e)
                retry = xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[2]/div/button')
                retry.click()
                items = self.driver.find_elements_by_tag_name("div")
                for item in items:
                    if str(item.text) == "Larry Thatcher":
                        item.click()
                        scrape(self.driver.page_source)
                        
                        alside_btn.click()
            except:
                try:
                    items = self.driver.find_elements_by_tag_name("div")
                    for item in items:
                        if str(item.text) == "Larry Thatcher":
                            item.click()
                            scrape(self.driver.page_source)
                            
                            alside_btn.click()
                            sleep(1)
                except:
                    print("all other tries have failed, attempting to restart...")
                    alside_btn = xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[10]/div')
                    alside_btn.click()
                    

            
    

driver = Driver()
driver.auto()