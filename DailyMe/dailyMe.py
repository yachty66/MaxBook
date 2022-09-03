from datetime import date
import cv2
import markdown

'''
- [x] folder
- [x] make image with current date and add to folder
- [x] find out how to add links for daily image as link (with link to respective image so that this gets displayed) to html file 
- [x] create python file for that 
- [x] test if it works
- [ ] add link to of html to home.md 
- [ ] create crontab from python for that
'''

'''
write on top of file image and above image date

create md file -- add link to image -- convert to html everyday when image was uploaded


link to html page is embedded in markdown. it exists a javascript file which adds based on how many images exist the name of the file as new link in html file 

can I do this with python? for sure! lets figure that out in python 

make image --> save image to folder with current date --> create link to site maxhager.xyz/dailyMe --> create link to site maxhager.xyz/dailyMe/2019-01-01 (site which lists all images from that day)

create cronjob directly from python script - run it every day 3pm - get email if it fails 

'''


def test():
    today = date.today()
    print(today)


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
