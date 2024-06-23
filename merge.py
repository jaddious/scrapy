# opens the images of each project and merges side by side them in a lower resolution image

import os
from PIL import Image
import numpy as np

projects = os.listdir("./projects_archive")

for project in projects:
    # if the project is not a folder, skip it:
    if not "." in project:
        if not os.path.exists("./projects_archive/"+project+"/merged_planches.png"):
            try:
                # get the images from the planches folder:
                images = os.listdir("./projects_archive/"+project+"/planches/")
                # if image does not have dexkstop.ini, remove it:
                for image in images:
                    if "desktop.ini" in image:
                        images.remove(image)
                print(len(images))
                # create a new image:
                img1 = Image.open("./projects_archive/" +
                                  project+"/planches/"+images[0])
                width = img1.width

                # create a new image with the height of the images and the width of the images * the number of images
                img = Image.new('RGB', (width*len(images), img1.height))

                # paste the images side by side:

                for i in range(len(images)):
                    img1 = Image.open("./projects_archive/" +
                                      project+"/planches/"+images[i])
                    img.paste(img1, (i*width, 0))

                # resize the image:
                img = img.resize((int(img.width/3), int(img.height/3)))

                # save the image:
                img.save("./projects_archive/"+project+"/merged_planches.png")

                # delete the planches folder and its contents:
                # os.system("rm -rf ./projects_archive/"+project+"/planches")
            except Exception as e:
                print(e)
                pass
