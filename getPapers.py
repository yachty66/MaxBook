'''
1. make a default folder for where papers saved from google chrome get added to - 
2. import data from mendeley
3. setup script which gets every day 00:00 the content of my read papers and adds them to papers read section on my personal website

4. 

'''
from datetime import date
from re import I
from turtle import title
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
    print(len(title))
    return title, date, doi

def writeToGsheet():
    gc = gspread.service_account(filename='papertracker.json')
    sh = gc.open_by_key("1noxRUYLUErYRgLNqh8eCceh41bSaRSQXW-Pz3WBKUL8")
    worksheet = sh.sheet1
    #adding data from to respective cells A2-An: title B2-Bn: datadded C2-Cn: DOI
    #missing two paper 
    title, date, doi = zotData()
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
    writeToGsheet()
    #zotData()
