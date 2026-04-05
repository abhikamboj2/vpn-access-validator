from smtplib import SMTP
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
load_dotenv()



Email_Password=os.getenv('Email_Password')
Reciver_Email_Address=os.getenv('Reciver_Email_Address')
Email_Address=os.getenv('Email_Address')



def Email_Automation(issues):
    if not issues:
        print("✅ No issues, email not sent")
        return

     with SMTP('smtp.gmail.com', 587) as smtp:
             smtp.ehlo()
             smtp.starttls()
             smtp.ehlo()
             smtp.login(Email_Address,Email_Password)
             body=''
             for i in issues:
                 zipc=i['zip']
                 flow=i['flow']
                 status=i['status']
                 body+= f"Zip: {zipc} | Flow: {flow} | Status: {status}\n"
             subject='Issue Occured in Daily VPN Sanity Check'

             msg=f'Subject: {subject}\n\n {body}'

             smtp.sendmail(Email_Address,Reciver_Email_Address,msg)
             logger.info('Mail is sent successfully')
       