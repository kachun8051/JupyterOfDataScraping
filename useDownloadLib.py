
import sys
sys.path.append("C:\\PythonLibs")
from myModule import DownloadImage
# use user input local folder
url = 'http://goodview.125mb.com/photostyle.html'
localpath = 'C:\\Downloads\\goodview_photo'
objDL = DownloadImage(url, localpath)
objDL.download()