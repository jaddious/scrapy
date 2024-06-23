import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


# get all the competition divs from the mainpage.html

print("hello")


data = pd.DataFrame()

# load to bs4

with open("./mainpage_archive.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# get all the competition divs

competition_divs = soup.find_all(
    "li", class_="filtrable")

# for each competition div get the img, href, title, and description
df = pd.DataFrame()

index = 0

for div in competition_divs:
    # get the a tag
    print(div.find("a"))
    a_tag = div.find("a")
    url = a_tag["href"]
    # get the div class title
    title = div.find("div", class_="title").text
    place = div.find("div", class_="place").text
    sessionid = div.find("span", class_="sessionid").text

    # add to the dataframe
    df = pd.concat([df, pd.DataFrame(  # create a dataframe
        {"url": [url], "title": [title], "place": [place], "sessionid": [sessionid]})])

    index += 1

# export to excel:

df.to_excel("europan_competitions_archive.xlsx")

for index, row in df.iterrows:
    # get the html from the url colomun and save in in a folder with the project name and the session id
    html = requests.get(row["url"]).text
    with open("./projects_archive/" + row["sessionid"] + ".html", "w", encoding='utf-8') as fp:
        fp.write(html)
