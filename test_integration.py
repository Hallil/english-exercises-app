import xmlrpc

# make an object to represent the xml-rpc server
server_url = "http:/localhost:5555/selenium-driver/RPC2"
app = xmlrpc.ServerProxy(server_url)

app.setTimeout(15)

import os

os.system('\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\"'
          + 'http://localhost:5555/selenium-driver/SeleneseRunner.html')
print (app.open('http://localhost:5555/AUT/000000A/http/www.google.com/'))
print (app.verifyTitle('Google'))
print (app.type('q', 'Selenium ThoughtWorks'))
print (app.verifyValue('q', 'Selenium ThoughtWorks'))
print (app.clickAndWait('btnG'))
print (app.verifyTextPresent('selenium.thoughtworks.com', ''))
print (app.verifyTitle('Google Search: Selenium ThoughtWorks'))
print (app.testComplete())
