from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def scrape_imdb():
    driver = webdriver.Chrome()
    url = "https://www.imdb.com/search/title/?year=2024&title_type=feature"
    driver.get(url)
    time.sleep(5)

    titles = []
    storylines = []

    movies = driver.find_elements(By.CLASS_NAME, 'lister-item')
    for movie in movies:
        try:
            title = movie.find_element(By.TAG_NAME, 'h3').text.split('\n')[0]
            storyline = movie.find_element(By.CLASS_NAME, 'text-muted').text
            titles.append(title)
            storylines.append(storyline)
        except Exception:
            continue

    driver.quit()
    df = pd.DataFrame({'Movie Name': titles, 'Storyline': storylines})
    df.to_csv("movies_2024.csv", index=False)
    print("Data saved to movies_2024.csv")

if __name__ == "__main__":
    scrape_imdb()
