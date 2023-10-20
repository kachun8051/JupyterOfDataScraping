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
# Regular Expression
### 基本功能運算子 1
| 運算子 | 說明 | 備註 |
| --- | --- | --- |
| `()` | 字符 **群組** |  |
| `\|` | 表示 **或者** |  |
| `?` | 表示 **沒有** 或 **1 個** 資料 | \[0, 1\] |
| `*` | 表示 **沒有** 或 **1 個以上** 資料 | \[0, 1, 2, 3, ...\] |
| `+` | 表示 **1 個以上** 資料 | \[1, 2, 3, ...\] |
| `\` | 表示後續字元作一般符號處理 | escape character |

### 基本功能運算子 2
| 運算子 | 說明 | 備註 |
| --- | --- | --- |
| `[]` | 自訂字符 **群組** | 例如: \[axe\] 表示符合 a 或 x 或 e |
| `[^]` | 自訂 **排除** 字符群組 | 例如 \[^axe\] 表示 _排除_ a 或 x 或 e |
| `[-]` | 字符群組 **範圍** | 例如 \[0-9\] 表示 _數字_ 0~9，\[a-z\] 表示字母 a ~ z |

### 字符類別
| 代號 | 說明 | 等同 |
| --- | --- | --- |
| `\d` | 數字 0 ~ 9 | \[0-9\] |
| `\D` | **不是** 數字 0 ~ 0 | \[^0-9\] |
| `\w` | 英文字母、數字及底線符號 | \[0-9A-Za-z\] |
| `\W` | **不是** 英文字母、數字及底線符號 | \[^0-9A-Za-z\] |
| `\s` | 空格、定位點及換行符號 | \[\\t\\r\\n\\f\] |
| `\S` | **不是** 空格、定位點及換行符號 | \[^ \\t\\r\\n\\f\] |

### 範圍類別
| 代號 | 說明 | 例如 |
| --- | --- | --- |
| `{x}` | 重複 x 個項目 | match = re.compile(r'(Ha){4}') |
| `{x,}` | 重複 x 個或以上項目 | match = re.compile(r'(Ha){4,}') |
| `{,y}` | 重複 0 至 y 個項目 | match = re.compile(r'(Ha){,4}') |
| `{x,y}` | 重複 x 至 y 個項目 | match = re.compile(r'(Ha){2,6}') |
| `^data` | 以 data 為 **首** 的字串 |  |
| `data$` | 以 data 為 **結尾** 的字串 |  |
| `data$` | 以 data 為 **結尾** 的字串 |  |
