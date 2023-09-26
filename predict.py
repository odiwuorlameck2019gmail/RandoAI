from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager  
from bs4 import BeautifulSoup 
import webbrowser

driver=webdriver.Chrome()
driver.get("http://127.0.0.1:8000/account/login/?next=/account/home/")
button=driver.find_element_by_css_selector("input[type='submit']")
button.click()


# url="https://www.worldometers.info/"
# driver=webdriver.Chrome(ChromeDriverManager().install())  
# driver.maximize_window()    
# driver.get(url)
# soup=BeautifulSoup (driver.page_source,'xml')
# num=soup.select_one('div#c49>div>span.counter-number')
# print(num.text)



