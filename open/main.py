import subprocess
import pathlib

doc_home = "https://developer.chrome.com/docs/extensions/mv3/getstarted/"
ExtensionsPath = f"{pathlib.Path.home()}/snap/chromium/common/chromium/Default/Extensions"

def openPage(link):
    subprocess.Popen(["xdg-open", f"{link}"])

def openInFileManager():
    subprocess.Popen(["xdg-open", ExtensionsPath])

if __name__ == '__main__':
    openPage(doc_home)
    openInFileManager()
