#Web scraping premier league player data from FBREF with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://fbref.com/en/comps/9/stats/Premier-League-Stats")

driver.implicitly_wait(0.5)

def scrape_player_info():

    time.sleep(1)
    try: #Check if the button can be found. If so, click
        driver.find_element(By.ID, "meta_more_button")
        more_info_button = driver.find_element(By.ID, "meta_more_button")
        more_info_button.click()
    except NoSuchElementException: #If no such element exists, pass
          pass

    #Select necessary html elements for player info
    player_profile = driver.find_element(By.CSS_SELECTOR, "#info")
    individual_name = player_profile.find_element(By.TAG_NAME, 'h1')
    individual_stats = player_profile.find_elements(By.TAG_NAME, 'p')

    #Select necessary html elements to find image source link
    locate_picture = player_profile.find_element(By.CLASS_NAME, 'media-item img')
    individual_picture = locate_picture.get_attribute('src')

    #Print data at selected html elements
    print(individual_name.text)
    print(individual_picture)
    for i in range(1,6):
            print(individual_stats[i].text)

    #Go back to page with all players
    driver.back()

scroll_to_players = driver.find_element(By.XPATH, '//*[@id="stats_standard_sh"]')
driver.execute_script("return arguments[0].scrollIntoView();", scroll_to_players)
time.sleep(1)

select_table = driver.find_element(By.XPATH, '//*[@id="stats_standard"]/tbody')
select_player = select_table.find_elements(By.TAG_NAME, 'tr')

for i in range(0, len(select_player)):
    if i == 2:
         time.sleep(5)
         modal = driver.find_element(By.ID, "modal-container")
         webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    elif i > 10:
         driver.execute_script("arguments[0].scrollIntoView();", select_player[i - 3])
    else:
         pass

    try: 
        select_player[i].find_element(By.TAG_NAME, 'a').click()
        scrape_player_info()
        select_table = driver.find_element(By.XPATH, '//*[@id="stats_standard"]/tbody')
        select_player = select_table.find_elements(By.TAG_NAME, 'tr')
    except NoSuchElementException:
         pass

driver.quit()

# TODO
# CLEAN DATA
#PUT DATA INTO ARRAY