from selenium import webdriver 


class webdriverBase(object):

    def __init__(self):
        # TODO: add config parameter
        # self.chrome = webdriver.Chrome()
        pass

    def chromeDefine(self,url):
        chrome = webdriver.Chrome()
        chrome.get(url)
        chrome.maximize_window()


# chrome_1 = webdriverBase()
supply = webdriverBase().chromeDefine("https://vhsupply.staging.viewchain.net")
# hosp = webdriverBase().chromeDefine("https://hospital.staging.viewchain.net")

