import pandas as pd
import os
from PIL import Image
import requests
from io import BytesIO
# import beautiful soup
from bs4 import BeautifulSoup

data = pd.read_excel(
    "europan_competitions_archive.xlsx")
dir = "./projects_archive"
# for each competition, create a folder inside the projects folder with the name of the competition

# get the
for index, row in data.iterrows():
    title = row["title"]
    with open("./projects_archive/"+str(index)+".html", "w", encoding='utf-8') as fp:
        # read the html as soup:
        soup = BeautifulSoup(requests.get(row["url"]).text, 'html.parser')

    div = soup.find("div", class_="projets-planches")
    # get the a tags:
    a_tags = div.find_all("a")
    # for each a tag, get the href and download the image
    # create the dir to hold the images:
    try:
        os.mkdir("./projects_archive/"+str(index))
        os.mkdir("./projects_archive/"+str(index)+"/planches")

        print("created dir: "+str(index))

        for a_tag in a_tags:
            print(a_tag)
            # get the href:
            href = "https://www.europanfrance.org/" + a_tag["href"]
            # get the image:
            img = Image.open(BytesIO(requests.get(href).content))
            num = a_tag["num"]
            # save the image:
            print("saving image: "+str(num)+".png")
            img.save("./projects_archive/"+str(index) +
                     "/planches/"+str(num)+".png")
            print("saved image: "+str(num)+".png")

        # save the html file to the new folder:
        with open("./projects_archive/"+str(index)+"/index.html", "w", encoding='utf-8') as fp:
            fp.write(str(soup))
    except:
        pass
