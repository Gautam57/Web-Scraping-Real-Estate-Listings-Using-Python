from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd


TYPES = ['Apartment', 'House']
POSTAL_CODE = ['20457']

with open('javascripts/totalPages.js', 'r', encoding='utf-8') as file:
            total_pages = file.read()
with open('javascripts/enterPostalCode.js', 'r', encoding='utf-8') as file:
            Enter_Postcode = file.read()
with open('javascripts/typeSelection.js', 'r', encoding='utf-8') as file:
            type_selection = file.read()
with open('javascripts/clickOnSearch.js', 'r', encoding='utf-8') as file:
            click_on_search = file.read()
with open('javascripts/clickOnNextPage.js', 'r', encoding='utf-8') as file:
            click_on_next_page = file.read() 
with open('javascripts/getData.js', 'r', encoding='utf-8') as file:
            get_data = file.read()

def fetch_price_area(postalcode, type):
    success = False
    totalpages = driver.execute_script(total_pages)
    print('Total pages:', totalpages)
    # Loop through all pages
    for i in range(1, int(totalpages) + 1):
        print(f'Page {i} of {totalpages}')
        currentpagedata = driver.execute_script(get_data)
        # print('Current page data:', currentpagedata)
        if currentpagedata:
            split_data = currentpagedata.split('|')
            for i in range(len(split_data) - 1):
                rowsvalues = split_data[i].split(';')
                price = rowsvalues[0]
                area = rowsvalues[1]
                result.loc[len(result)] = [postalcode,price, area, type]
        if int(totalpages) > 1:
            # click on the next page button
            driver.execute_script(click_on_next_page)
            print('Next page button clicked')
            time.sleep(5)
        success = True
    return success


result = pd.DataFrame(columns=['PostalCode','Price', 'Area','Type'])

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
prefs = {
    "translate_whitelists": {"de": "en"},  # from German to English
    "translate": {"enabled": True}
}
chrome_options.add_experimental_option("prefs", prefs)



driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.immobilienscout24.de/')
time.sleep(10)           
# Loop through the postal codes
for postalcode in POSTAL_CODE:
    for n,type in enumerate(TYPES):
        print(f'Processing postal code: {postalcode} and type: {type}')
        # enter the postal code
        if n == 0:
            driver.execute_script(Enter_Postcode,postalcode)
            print('Postal code entered')
            time.sleep(10)
        # select the type of property       
        driver.execute_script(type_selection,type)
        print('Type selected')
        time.sleep(5)
        # click on the search button       
        driver.execute_script(click_on_search)
        print('Search button clicked')
        time.sleep(10)

        allDataCollectecd = fetch_price_area(postalcode, type)
        if allDataCollectecd:
            print('All data collected successfully')
            driver.get('https://www.immobilienscout24.de/')
            time.sleep(10)
        else:
            print('Failed to collect data')




# Save the result to a CSV file
result.to_csv('immobilien.csv', index=False, encoding='utf-8-sig')

# time.sleep(200)
driver.quit()
