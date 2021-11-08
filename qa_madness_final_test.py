from selenium import webdriver

search_xpath = '/html/body/div[2]/div/header/div/div[1]/div[2]/div/form/input'
search_button_xpath = '/html/body/div[2]/div/header/div/div[1]/div[2]/div/form/button'
product_xpath = '/html/body/div[2]/div/main/section[2]/div/div/div/ul/li'
path_to_webdriver = '/Users/ysenkiv/Code/access files/chromedriver'
webdriver = webdriver.Chrome(executable_path=path_to_webdriver)
webdriver.maximize_window()
webdriver.get('https://www.board-game.co.uk/')


def try_search(multiplier):
    webdriver.find_element_by_xpath(search_xpath).send_keys('a' * multiplier)
    webdriver.find_element_by_xpath(search_button_xpath).click()
    webdriver.find_element_by_xpath(search_xpath).clear()
    if 'query' in webdriver.current_url:
        print(f'{"a" * multiplier} works')  # here should be return True
    else:
        print(f'{"a" * multiplier} does not work') # here should be return False


for x in range(1, 4):
    try_search(x)




