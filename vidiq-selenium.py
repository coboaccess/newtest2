from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from datetime import datetime
# Set up the WebDriver (use the appropriate driver for your browser, e.g., ChromeDriver)
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://app.vidiq.com/channels/919ec64a-dbbc-4e12-80c4-07168df38b9f/keywords/overview/")  # Replace with the actual URL

    # Wait for the page to load (optional, depending on the website's loading time)
    time.sleep(2)  # Adjust the delay as needed

    keywords_to_search = [
        'digital marketing',
'social media marketing',
'content marketing',
'email marketing',
'affiliate marketing',
'influencer marketing',
'marketing strategy',
'marketing automation',
'search engine optimization',
'online marketing',
'marketing plan',
    ]


    email_box = driver.find_element("id", "email")
    email_box.send_keys("smartvidboost@gmail.com")
    password_box = driver.find_element("id", "password")
    password_box.send_keys("ohappydays@123")

    login_button = driver.find_element("css selector", '[data-testid="login-button"]')
    login_button.send_keys(Keys.ENTER)
    time.sleep(5)
    # Locate the input element by its ID
    try:
        search_box = driver.find_element("id", "keyword-search")
    except:
        print("Please login. Waiting 60 s")
        """
        smartvidboost@gmail.com
        ohappydays@123
        """
        time.sleep(60)
        search_box = driver.find_element("id", "keyword-search")

    for keyword_to_search in keywords_to_search:
        search_box = driver.find_element("id", "keyword-search")
        time.sleep(3)
        # Enter a string into the input field
        search_box.clear()  # Replace with your desired string
        search_box.send_keys(keyword_to_search)  # Replace with your desired string
        time.sleep(1)

        # Simulate pressing the Enter key
        search_box.send_keys(Keys.ENTER)

        buttons = [
            "related-keywords",
            "matching-terms",
            "questions",
        ]

        time.sleep(2)
        for button in buttons:
            button_to_click = driver.find_element("xpath", f'//*[@value="{button}"]')
            button_to_click.click()
            time.sleep(2)
            table = driver.find_element("id", f"{button}-table")
            rows = table.find_elements("tag name", "tr")

            table_data = []
            for row in rows:
                cells = row.find_elements("tag name", "td")
                if cells:  # Skip header or empty rows
                    # Extract and clean cell values
                    if button == "related-keywords":
                        keyword = cells[1].text.strip()
                        related_score = cells[2].text.strip()
                        search_volume = cells[3].text.strip()
                        competition = cells[4].text.strip()
                        overall = cells[5].text.strip()
                        number_of_words = cells[6].text.strip()

                        row_object = {
                            "keyword": keyword,
                            "related_score": related_score,  # float(related_score) if related_score else None,
                            "search_volume": search_volume,  # search_volume.replace(",", ""),  # Remove commas
                            "competition": competition,
                            "overall": overall,  # int(overall) if overall else None,
                            "number_of_words": number_of_words,  # int(number_of_words) if number_of_words else None,
                        }
                    else:
                        keyword = cells[1].text.strip()
                        search_volume = cells[2].text.strip()
                        competition = cells[3].text.strip()
                        overall = cells[4].text.strip()
                        number_of_words = cells[5].text.strip()
                        
                        row_object = {
                            "keyword": keyword,
                            "search_volume": search_volume,  # search_volume.replace(",", ""),  # Remove commas
                            "competition": competition,
                            "overall": overall,  # int(overall) if overall else None,
                            "number_of_words": number_of_words,  # int(number_of_words) if number_of_words else None,
                        }

                    table_data.append(row_object)

            # Print the extracted table data as a list of objects
            with open(f"{keyword_to_search}-{button}-27-12-2024.txt", "w", encoding="utf-8") as file:
                for item in table_data:
                    if button == "related-keywords":
                        line = (
                            f"Keyword: {item['keyword']}, "
                            f"Related Score: {item['related_score']}, "
                            f"Search Volume: {item['search_volume']}, "
                            f"Competition: {item['competition']}, "
                            f"Overall: {item['overall']}, "
                            f"Number of Words: {item['number_of_words']}\n"
                        )
                    else:
                        line = (
                            f"Keyword: {item['keyword']}, "
                            f"Search Volume: {item['search_volume']}, "
                            f"Competition: {item['competition']}, "
                            f"Overall: {item['overall']}, "
                            f"Number of Words: {item['number_of_words']}\n"
                        )
                    file.write(line)
                    # print(item)
    
    # pprint("="*50)
    # pprint(table_data)
    # pprint("="*50)
    # Optionally, wait to observe the result
    time.sleep(15)  # Adjust the delay as needed

except Exception as e:
    print("Exception!")
    print(e.__str__())
    time.sleep(5)
finally:
    # Close the browser
    # driver.quit()
    pass