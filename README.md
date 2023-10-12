# JupyterOfDataScraping
Use Python to scrap data from the internet
# For DownloadImages2 Demo
This example shows how to import a custom class. 
The steps are:
1. Create a library folder i.e. C:\\PythonLibs
2. Copy the class (i.e. DownloadImage) scripts in DownloadImages3.ipynb.
3. Save it as file name myModule.py
4. Put it in the library folder i.e. C:\\PythonLibs\\myModule.py
5. In any Python IDE such as Jupyter Notebook or IDLE, import this library by:
   ```
   import sys
   sys.path.append("C:\\PythonLibs")   
   ```
6. Use the library by:
   ```
   from myModule import DownloadImage
   url = 'http://goodview.125mb.com/photostyle.html'
   objDL = DownloadImage(url)
   objDL.download()
   ```
7. If the custom module is put in the same folder as the python file. The code in step 5 is replaced by:
   ```
   import sys
   sys.path.append(".")
   ```
8. If the custom module myModule.py is put in the path: C:\\Python39\\kachunLibs which is added in the environment variable's Path
   
   ![Environment Variables -> System Variables -> Path](./images/envvar_path.png)

9. import the library directly without using sys
   ```
   from myModule import DownloadImage
   url = 'http://goodview.125mb.com/photostyle.html'
   objDL = DownloadImage(url)
   objDL.download()
   ```
