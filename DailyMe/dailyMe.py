from datetime import date
import cv2
import markdown

import time

def today():
    t = date.today()
    return t


def makeImage():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    t = today()
    ret, frame = cam.read()

    # make image smaller
    frame = cv2.resize(frame, (0, 0), fx=0.35, fy=0.35)
    img_name = "/Users/maxhager/Projects2022/MaxBook/DailyMe/images/{}.png".format(t)
    cv2.imwrite(img_name, frame)
    #print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()


def getFileContent():
    content = []
    with open("/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.md") as file:
        lines = file.readlines()
    for line in lines:
        content.append(line)
    return content


def emptyFile():
    with open("/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.md", "w") as file:
        file.write("")


def addImage():
    content = getFileContent()
    # need to add first md link and than image at the beginning of the file
    emptyFile()
    t = str(today()) + "\n\n"
    image = "![](images/" + str(today()) + ".png)\n\n"
    content.insert(0, image)
    content.insert(0, t)
    # add image from makeImage() to images.md
    with open("/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.md", "a") as file:
        for line in content:
            file.write(line)


def convertToHtml():
    markdown.markdownFromFile(
        input='/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.md',
        output='/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.html'
    )


if __name__ == "__main__":
    makeImage()
    addImage()
    convertToHtml()
