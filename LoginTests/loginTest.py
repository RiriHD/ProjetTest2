from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import webbrowser
#creer une variable pour déclencher le driver
def config_driver(login,pwd): 
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # # Bypass OS security model
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')
    driver.get("http://192.168.77.75:2500/auth/login")
    driver.find_element_by_xpath('/html/body/app-root/app-auth/div/app-login/div[1]/div/form/div/div[2]/input').send_keys(login)
    driver.find_element_by_xpath('/html/body/app-root/app-auth/div/app-login/div[1]/div/form/div/div[3]/div/input').send_keys(pwd)
    driver.find_element_by_xpath('/html/body/app-root/app-auth/div/app-login/div[1]/div/form/div/div[4]/button[1]').click()
    time.sleep(3)
    url=driver.current_url
    
    driver.close()
    return(url)

def valid_login(login,pwd):
    titre=config_driver(login,pwd)
    if titre=='http://192.168.77.75:2500/main/dashboard':
        print("valide login pass")
    else:
        print("valide login fail")

def invalid_login(login,pwd):
    titre=config_driver(login,pwd)
    if titre=='http://192.168.77.75:2500/main/dashboard':
        print("invalide login fail")
    else:
        print("invalide login pass")

if __name__ == '__main__':
    login="agts.etc@gmail.com"
    pwd="AZERTY123"
    print(valid_login(login,pwd))
    login="invalide@gmail.com"
    pwd="AZERTY123"
    print(invalid_login(login,pwd))