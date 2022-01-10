import zipfile
import re
zipname = "D:\\001\\ziptest\\123.zip"
while True:
    if zipname != "D:\\001\\ziptest\\zip.zip":
        ts1 = zipfile.ZipFile(zipname)
        res = re.search('[0-9]*',ts1.namelist()[0])
        print(res.group())
        passwd = res.group()
        ts1.extractall("D:\\001\\ziptest",pwd=passwd)
        zipname = "D:\\001\\ziptest\\"+ts1.namelist()[0]
    else:
        print("find")
