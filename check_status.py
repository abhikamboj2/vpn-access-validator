import logging
logger = logging.getLogger(__name__)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def check_status(driver,Base_URL,wait,Zipcode,flow):
    logger.info(f'{flow} | Zipcode:{Zipcode} started' )
    try:
        driver.get(Base_URL)
        if flow=='Home': 
            elements = driver.find_elements(By.XPATH, "//a[@data-dl-cat='Quote - Home']")
            home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@data-dl-cat='Quote - Home'])[last()]")))
            home_btn.click()
            Zipcode_Search=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='zip' and contains(@data-dl, 'Quote - Home')]")))
        else:
            btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-dl-cat='Quote - Auto']")))
            btn.click()
            Zipcode_Search=wait.until(EC.element_to_be_clickable((By.NAME, "zip")))
                       
        
        Zipcode_Search.clear()
        Zipcode_Search.send_keys(Zipcode)
        Zipcode_Search.send_keys(Keys.RETURN)
        wait.until(lambda d: "Access Denied" in d.page_source or "policy" in d.current_url)

        if "Access Denied" in driver.page_source:
            status = "BLOCKED"
            logger.info(f"{flow} | {Zipcode} BLOCKED ✅")
        else:
            status = "NOT_BLOCKED"
            logger.error(f"{flow} | {Zipcode} NOT BLOCKED ❌")

        return status
    except Exception as e:
        logger.error(f"{flow} | {Zipcode} ERROR: {str(e)}")
        return "ERROR"    