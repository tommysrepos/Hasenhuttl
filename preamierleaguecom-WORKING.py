from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/players')
# driver.fullscreen_window()
driver.execute_script("window.moveTo(0,0); window.resizeTo(screen.width,screen.height);")
time.sleep(2)

#Close cookies preferences modal
cookies_modal = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
cookies_modal.click()
time.sleep(3)

#Store all scraped date in this list
playerList = []

#Player scraping directions + cleaning data
def scrape_player_info():
    #Get first and last name
    fname = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/h1/div/div[1]')
    lname = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/h1/div/div[2]')

    #Combine for list name value
    player_name = fname.text + ' ' + lname.text

    #Get current player's team
    player_team = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[2]/section[1]/div[2]/div[2]/a').get_attribute('text')

    #Get current player's nationality
    player_nationality = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[2]/section[1]/div[1]/div[1]/div[2]/span[2]').get_attribute('innerHTML')

    #Get current player's position
    player_position = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[2]/section[1]/div[3]/div[2]').get_attribute('innerHTML')

    #Get current player's age
    player_age = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[2]/section[1]/div[1]/div[2]/div[2]').get_attribute('innerHTML').strip() #remove white spaces

    #Slice off uneeded characters
    player_age = player_age[13:15]

    #Get current player's jersey number
    player_number = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/div').get_attribute('innerHTML')

    #Get current player's picture
    player_image = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[1]/img').get_attribute('src')

    #Select container for current player's team history
    player_history = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[3]')

    #Get a list of all teams from current player's team history
    player_previous_team = player_history.find_elements(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div[3]/table/tbody/tr/td/a/span[3]')

    #Put all current player's date into a dictionary with properly labeled keys
    current_player = {}
    current_player['name'] = player_name
    current_player['team'] = player_team.strip()
    current_player['nationality'] = player_nationality.strip()
    current_player['position'] = player_position.strip()
    current_player['age'] = player_age.strip()
    current_player['number'] = player_number.strip()
    current_player['image'] = player_image
    current_player['previousTeam'] = []
    for i in range(0, len(player_previous_team)):
        if player_previous_team[i].get_attribute('innerHTML') != player_team.strip() and player_previous_team[i].get_attribute('innerHTML') not in current_player['previousTeam']:
            current_player['previousTeam'].append(player_previous_team[i].get_attribute('innerHTML'))
    playerList.append(current_player)
    print(playerList)

#get player links
player_links = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div/table/tbody/tr/td/a')

scroll_distance = 50
scroll_2 = 5
for i in range(0,1000):
    
    player_links[i].click()
    time.sleep(1)
    scrape_player_info()
    driver.back()
    time.sleep(1)
    player_links = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div/table/tbody/tr/td/a')
    if i > 3:
        # driver.execute_script("arguments[0].scrollIntoView();", player_links[i - 3])
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(2)
        # driver.execute_script(f"window.scrollBy(0, {scroll_2});")
        # time.sleep(2)
        player_links = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div/table/tbody/tr/td/a')
        # driver.execute_script(f"window.scrollBy(0, {scroll_2});")
        # time.sleep(2)
        player_links = driver.find_elements(By.XPATH, '//*[@id="mainContent"]/div[2]/div/div/div/table/tbody/tr/td/a')
    print('current iteration: '+ str(i))
    print('size of player_links: '+ str(len(player_links)))