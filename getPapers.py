from pyzotero import zotero
import gspread
import config


def zotData():
    zot = zotero.Zotero(config.library_id, config.library_type, config.api_key)
    title = []
    date = []
    doi = []
    items = zot.collection_items_top("FRG3E6UR")
    for i in range(len(items)):
        try:
            title.append(items[i]["data"]["title"])
            date.append(items[i]["data"]["dateAdded"])
            doi.append(items[i]["data"]["DOI"])
        except KeyError:
            doi.append("")
    return title, date, doi


def cleanDate(date):
    for i in range(len(date)):
        date[i] = date[i][:10]
    return date


def writeToGsheet():
    gc = gspread.service_account(filename='/Users/maxhager/Projects2022/MaxBook/papertracker.json')
    sh = gc.open_by_key(config.sheet_key)
    worksheet = sh.sheet1
    title, date, doi = zotData()
    date = cleanDate(date)
    curr = ""
    s = "ABC"
    for i in range(len(title)):
        for j in s:
            if j == "A":
                curr = title
            elif j == "B":
                curr = date
            elif j == "C":
                curr = doi
            worksheet.update(j+str(i+2), curr[i])


if __name__ == '__main__':
    print("hallo")
    writeToGsheet()
