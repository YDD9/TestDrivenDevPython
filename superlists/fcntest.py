from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Welcome to Django' in browser.title

# browser.get('https://www.google.com/')
# assert 'Welcome To Zscaler Directory Authentication' in browser.title

print(browser.title)