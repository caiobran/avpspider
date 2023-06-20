from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# initialize selenium driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('start-maximized')
executable_path = ChromeDriverManager().install()
chrome_service = ChromeService(executable_path=executable_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to AVP America page
url = 'https://avpamerica.com/VA-Beach-Volleyball-Player-Rankings.aspx'
driver.get(url)