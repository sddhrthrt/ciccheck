from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://onlineservices-servicesenligne-cic.fjgc-gccf.gc.ca/mycic/gccf?lang=eng&idp=gckey&svc=/mycic/start"

driver = os.environ.get('DRIVER', 'phantomjs')
if driver == 'geckodriver':
    print("Using firefox:")
    dr = webdriver.Firefox()
else:
    print("Using PhantomJS:")
    dr = webdriver.PhantomJS()

dr.get(baseurl)

xpaths = {
        'username': "//input[@id='token1']",
        'password': "//input[@id='token2']",
        'loginbtn': "//form[@id='login']//button",
        'continuebtn': "//input[@id='continue']",
        'question': "//label[@for='answer']//strong",
        'answer': "//input[@id='answer']",
        '_continuebtn': "//input[@id='_continue']",
        'completedapptable': "//table[@id='completedAppTable']",
          }

data = {
        'username': "##username##",
        'password': "##password##",
        'questions': {
            # format:
            # a unique searchword for the question: answer
            'favorite pet': 'pet name',
            'mother\'s': 'maiden name',
            # and so on for all your questions.
        }
        }

# convenience:
def findxpath(dr, path):
    return dr.find_element_by_xpath(path)

# login
uname = findxpath(dr, xpaths['username'])
pwd = findxpath(dr, xpaths['password'])

uname.clear()
uname.send_keys(data['username'])
pwd.clear()
pwd.send_keys(data['password'])

findxpath(dr, xpaths['loginbtn']).click()
print "Logging in..."

# continue
continuebtn = WebDriverWait(dr, 15).until(EC.presence_of_element_located((By.XPATH, xpaths['continuebtn'])))
continuebtn.click()
print "Pressed continue..."

# agree
continuebtn = WebDriverWait(dr, 20).until(EC.presence_of_element_located((By.XPATH, xpaths['_continuebtn'])))
continuebtn.click()
print "Pressed I agree..."

# find question
question = findxpath(dr, xpaths['question']).text
answer = findxpath(dr, xpaths['answer'])
for key, value in data['questions'].iteritems():
    if key in question:
        answer.clear()
        answer.send_keys(value)
        break

findxpath(dr, xpaths['_continuebtn']).click()
print "Answering question..."


# find application
print "Getting status..."
table = WebDriverWait(dr, 20).until(EC.presence_of_element_located((By.XPATH, xpaths['completedapptable'])))

# print results:
applications = table.find_elements_by_xpath(".//tr")[1:]
for idx, app in enumerate(applications):
    fields = [idx, ] + map(lambda e: e.text, app.find_elements_by_xpath(".//td")[3:6])
    print "Application %s from %s: status %s. (messages: %s)"%tuple(fields)

dr.quit()
