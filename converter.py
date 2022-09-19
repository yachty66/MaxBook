'''
1. m for converting md to hmtl
2. render htmkl and check if its the format which i wish to have
'''
import markdown
from git import Repo
# https://www.devdungeon.com/content/convert-markdown-html-python tutorial about Markdown Python


def convert():
    markdown.markdownFromFile(
        input='/Users/maxhager/Projects2022/MaxBook/home.md',
        output='/Users/maxhager/Projects2022/MaxBook/index.html',
        extensions=['toc'],
    )


def pushToGithub():
    repo_dir = ''
    repo = Repo(repo_dir)
    file_list = [
        "/Users/maxhager/Projects2022/MaxBook/converter.py",
        "/Users/maxhager/Projects2022/MaxBook/index.html",
        "/Users/maxhager/Projects2022/MaxBook/home.md",
        "/Users/maxhager/Projects2022/MaxBook/README.md",
        "/Users/maxhager/Projects2022/MaxBook/DailyMe/dailyMe.html",
        "/Users/maxhager/Projects2022/MaxBook/DailyMe/images/"
        
    ]
    commit_message = 'Update'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()


if __name__ == "__main__":
    convert()
    pushToGithub()
