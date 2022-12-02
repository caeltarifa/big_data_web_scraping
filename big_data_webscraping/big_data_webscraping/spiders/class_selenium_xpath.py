from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re

class selenium_scrapy:
    url_list=[]
 
    def driversetup(self):
        driver_location = '/usr/bin/chromedriver'
        binary_location = '/usr/bin/google-chrome'
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location
        #run Selenium in headless mode
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        #overcome limited resource problems
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("lang=en")
        #open Browser in maximized mode
        options.add_argument("start-maximized")
        #disable infobars
        options.add_argument("disable-infobars")
        #disable extension
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")
        options.add_argument("--disable-blink-features=AutomationControlled")
        prefs={'download.default_directory':'/media/big_data_webscraping'}
        options.add_experimental_option('prefs',prefs)
        
        driver = webdriver.Chrome(options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

        return driver
    
    def pagesource(self,url):
        driver = self.driversetup()
        driver.get(url)
        #soup = BeautifulSoup(driver.page_source)
        soup=driver.find_elements(By.XPATH, '//a[starts-with(@onclick, "SetCapitu")]' )
        self.url_list = []
        for a in soup:
            self.url_list.append(self.url_title(a.get_attribute('onclick')))
        driver.close()

    def url_title(self,t):
        replacements = [
            ("'",""),
            (")",""),
            ("(",""),
            (", ","/"),
            ("SetCapitulo",""),
        ]
        for x,y in replacements:
            t=t.replace(x,y)
        return t+'/'
        
    def click_element_bcentral(self, url):
        driver = self.driversetup()
        driver.get(url)

        #soup = BeautifulSoup(driver.page_source)
        soup=driver.find_elements(By.XPATH, '//*[@id="fsTable"]/div[1]/div[1]/button[5]' )[0]
        soup.click()
        button_before_click = soup.get_attribute('class')

        soup=driver.find_elements(By.XPATH, '//*[@id="btnIQYContinue"]' )[0]
        #soup.click()
        time.sleep(5)

        button_after_click = soup.get_attribute('class')

        return "before_click >>> " + str(button_before_click) + "    after click >>"+ str(button_after_click )
        
        driver.close()  

    def click_exploring_ine(self, url):
        driver = self.driversetup()
        driver.get(url)

        list_response = []
        dict_file = {}

        ## TITLE PANELS
        arr_title = driver.find_elements(By.XPATH, '//*[@id="Content_C007_Col00"]/div/div/div' )
        for title in arr_title:
            title.click()
            time.sleep(3)

            ## BUBTITLE PANELS
            arr_subtitle = driver.find_elements(By.XPATH, '//*[@id="Content_C007_Col01"]/div/div/div[4]/div/div/div' )
            for subtitle in arr_subtitle:
                subtitle.click()
                time.sleep(3)

                arr_link = driver.find_elements(By.XPATH, '//*[@id="Content"]/div[3]/div[3]//a' )
                for link in arr_link:

                    f_name = str(link.text)
                    *f_name,  format, size, dimension = re.split(r'[;,\s]\s*', f_name)
                    f_name = ' '.join(f_name)
                    
                    dict_file = {
                    'name' : title.text + " / " + subtitle.text, 
                    'file_name':f_name,
                    'file_format':format,
                    'file_size':size,
                    'file_dimension':dimension,
                    
                    'link': link.get_attribute('href')
                    }
                    list_response.append(dict_file)

        driver.close()  
        return list_response
      