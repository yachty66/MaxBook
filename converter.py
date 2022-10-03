import markdown
import subprocess
import config
# https://www.devdungeon.com/content/convert-markdown-html-python tutorial about Markdown Python


def convert():
    markdown.markdownFromFile(
        input='/Users/maxhager/Projects2022/MaxBook/home.md',
        output='/Users/maxhager/Projects2022/MaxBook/index.html',
        extensions=['toc'],
    )


def pushToGithub():
    subprocess.call(['git', 'add', '.'], cwd='/Users/maxhager/Projects2022/MaxBook')
    subprocess.call(['git', 'commit', '-m', 'update'], cwd='/Users/maxhager/Projects2022/MaxBook')
    subprocess.call(['git', 'push', 'https://{}@github.com/yachty66/MaxBook.git'.format(config.tokenGit)], cwd='/Users/maxhager/Projects2022/MaxBook')

if __name__ == "__main__":
    convert()
    pushToGithub()
