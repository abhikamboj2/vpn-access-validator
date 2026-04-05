from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



#import stuff
from zip_code import zip_codes
from check_status import check_status


# set up .env
from dotenv import load_dotenv
import os 
load_dotenv()
Base_URL=os.getenv('Base_URL')

if not Base_URL:
    raise ValueError("Base_URL not found in .env")

#set up selenium driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#set up logging 
import logging

os.mkdirs("logs",exist_ok=True)
logging.basicConfig(
    filename='logs/app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 
#this is logger object
logger = logging.getLogger(__name__)

flows=['Home','Auto']
result=[]
for flow in flows:
    for zipc in zip_codes:
        status=check_status(driver,Base_URL,wait,zipc,flow)

        result.append({"zip": zipc,
            "flow": flow,
            "status": status})
print(result)


#mail automation
from Email_automation import Email_Automation
issues=[r for r in result if r["status"]!='BLOCKED']

Email_Automation(issues)
driver.quit()








