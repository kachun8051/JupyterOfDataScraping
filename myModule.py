import os, requests
import shutil
from bs4 import BeautifulSoup
from datetime import datetime

# please put this file i.e. myModule.py in folder: C:\PythonLibs
class DownloadImage:
    def __init__(self, _url, _localfolder='C:\\Downloads\\Images'):
        self.url = _url        
        self.localfolder = _localfolder
        isChecked = self.checkfolder(self.localfolder)
        self.isLocalFolderExist = False
        if isChecked == False:
            print(f'Local folder: {self.localfolder} does NOT exist!')
            self.isLocalFolderExist = False
        else:
            if _localfolder == 'C:\\Downloads\\Images':
                print(f'Local folder (Default): {self.localfolder}.')
            else:
                print(f'Local folder: {self.localfolder}.')
            self.isLocalFolderExist = True
       
    @staticmethod
    def checkfolder(_folder):
        if not os.path.exists(_folder):
            try:
                os.makedirs(_folder)
                print(f'Folder: {_folder} is created!')
                return True
            except Exception as e:
                print(f"Exception: {e.message} {e.args}")
                return False
        else:
            return True
    
    def getDomain(self):
        _path = os.path.dirname(self.url)
        return _path
    
    def getImg(self):
        html = requests.get(self.url)
        html.encoding = 'UTF-8'
        sp = BeautifulSoup(html.text, 'html.parser')
        elems = sp.select('img')
        # print(type(elems))
        return elems
    
    @staticmethod
    def getImgName(_url):
        lst1 = _url.split('/')
        if len(lst1) == 0:
            return ''
        else:
            return lst1[len(lst1)-1]
       
    # download file non-stream
    def downloadImg(self, imgPath):    
        _imgFile = self.getImgName(imgPath)
        isChecked = self.checkfolder(self.localfolder)
        if isChecked == False:
            print(f'Local folder: {self.localfolder} does NOT exist!')
            return False
        _domain = self.getDomain()
        _headers = {'Referer': _domain}
        ans = requests.get(f'{_domain}/{imgPath}', headers=_headers)
        if not ans.status_code == requests.codes.ok:
            return False
        with open(f'{self.localfolder}\\{_imgFile}', 'wb') as myFile:
            for x in ans.iter_content(10240):
                myFile.write(x)
        return True
    
    # download file by stream
    def downloadImg2(self, imgPath):    
        _imgFile = self.getImgName(imgPath)
        isChecked = self.checkfolder(self.localfolder)
        if isChecked == False:
            print(f'Local folder: {self.localfolder} does NOT exist!')
            return False        
        _domain = self.getDomain()
        _headers = {'Referer': _domain}        
        res = requests.get(f'{_domain}/{imgPath}', stream=True, headers=_headers)
        if not res.status_code == requests.codes.ok:
            return False           
        with open(f'{self.localfolder}\\{_imgFile}', 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        return True
    
    def download(self):
        if self.isLocalFolderExist == False:
            print('Can not download to non-existing local folder!')
            return False
        lst = self.getImg()
        lst1 = []
        lst2 = []
        startDt  = datetime.now()
        print(f'Start download at: {startDt.strftime("%H:%M:%S")}') 
        for idx, x in enumerate(lst):
            val = x.get('src')
            fName = self.getImgName(val)
            if self.downloadImg2(val) == True:
                lst1.append(fName)
                print(f"{idx+1}/{len(lst)}: ({fName}) has downloaded.")
            else:
                lst2.append(fName)
                print(f"{idx+1}/{len(lst)}: ({fName}) has NOT downloaded!")
        endDt = datetime.now()
        print(f'Complete downloaded at: {endDt.strftime("%H:%M:%S")}')
        dur = endDt - startDt        
        print(f"{len(lst1)}/{len(lst)} has completed which spend {round(dur.total_seconds(), 3)} seconds.") 