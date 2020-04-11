from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.naver.com")
soup = BeautifulSoup(browser.page_source, "html.praser")