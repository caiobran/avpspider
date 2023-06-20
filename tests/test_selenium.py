import logging

logging.basicConfig(
    # filename='app.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("----- IMPORT LIBRARIES -----")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

# initialize selenium driver
logging.info("----- INITIALIZE CHROME DRIVER -----")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
# chrome_options.add_argument('start-maximized')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('disable-dev-shm-usage')

executable_path = ChromeDriverManager().install()
chrome_service = ChromeService(executable_path=executable_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to AVP America page
logging.info("----- OPEN URL -----")

url = 'https://avpamerica.com/VA-Beach-Volleyball-Player-Rankings.aspx'
driver.get(url)

# Wait for the "Refresh Rankings" button to load
wait = WebDriverWait(driver, 5)
locator = (By.XPATH, '//*[(@id = "btnSubmit")]')
el_refresh = wait.until(EC.element_to_be_clickable(locator))

# Click the "Refresh Rankings" button
el_refresh.click()

# Wait for table 2 (all avp players) to load
locator = (By.XPATH, '//*[@id="Table2"]')
wait.until(EC.presence_of_element_located(locator))

source_code = driver.page_source.encode('utf-8')

# Close Chrome
logging.info("----- CLOSE URL -----")

driver.quit()

# Save html file
filename = f'avpamerica.html'

with open(filename, 'wb') as f:
    f.write(source_code)

logging.info(f'Saved file {filename}')