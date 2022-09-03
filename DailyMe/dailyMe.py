from datetime import date
import cv2
import markdown

'''
- [x] folder
- [x] make image with current date and add to folder
- [x] find out how to add links for daily image as link (with link to respective image so that this gets displayed) to html file 
- [x] create python file for that 
- [x] test if it works
- [x] add link to of html to home.md 
- [ ] create crontab from python for that
'''



def today():
    t = date.today()
    return t


def makeImage():
    cam = cv2.VideoCapture(0)
    # todo can be removed?
    cv2.namedWindow("test")
    t = today()
    ret, frame = cam.read()
    # make image smaller
    frame = cv2.resize(frame, (0, 0), fx=0.35, fy=0.35)
    img_name = "images/{}.png".format(t)
    cv2.imwrite(img_name, frame)
    #print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()


def getFileContent():
    content = []
    with open("dailyMe.md") as file:
        lines = file.readlines()
    for line in lines:
        content.append(line)
    return content


def emptyFile():
    with open("dailyMe.md", "w") as file:
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
    with open("dailyMe.md", "a") as file:
        for line in content:
            file.write(line)


def convertToHtml():
    markdown.markdownFromFile(
        input='dailyMe.md',
        output='dailyMe.html'
    )


if __name__ == "__main__":
    makeImage()
    addImage()
    convertToHtml()
    # run should output date - image - [date](![2022-09-03](images/h.png))
    pass
