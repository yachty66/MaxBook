from datetime import date
import cv2
import markdown

'''
Notes:
    - tccutil reset Camera -> for reseting camera settings 
    open -a /Users/maxhager/Projects2022/MaxBook/DailyMe/test.app

- [x] folder
- [x] make image with current date and add to folder
- [x] find out how to add links for daily image as link (with link to respective image so that this gets displayed) to html file 
- [x] create python file for that 
- [x] test if it works
- [x] add link to of html to home.md 
- [ ] create crontab from python for that
- [ ] clean code and add readme

crontab every day 15:00 - first check if it works 
send message to mail if cronjob fails

problem is that I do not get the cronjob executed with the script I created
'''

import time

def today():
    t = date.today()
    return t


def makeImage():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    t = today()
    ret, frame = cam.read()
    #frame has in crontab no image. why?
    #issue is cron does not have access to camera. possible workaround is https://apple.stackexchange.com/questions/384310/how-do-i-configure-camera-and-microphone-permission-on-macos-mojave
    #other workaround is using applescript to take a picture and run it every 
    #could write applescript and run this script and than add it to crontab
        #i need a different terminal from where i run the script and use iterm for that
        #so i create a apple script which calls py script with iterm
        #before doing that I execute this py script with iterm
    #other workaround is to run crontab manually. to much work
    #writing a cronjob who executes a script from iterm2
    


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
    print("SHOULD APPEAR")
    makeImage()
    addImage()
    convertToHtml()
