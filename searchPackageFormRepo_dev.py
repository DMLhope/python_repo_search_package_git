#!/usr/bin/python3
#-- coding:UTF-8 --
import sys
import urllib.request
import urllib.parse
import string
import re
#返回拼接好的url地址
def url_return():
    #仓库地址
    repo_url = "http://10.2.10.135/uos-sw64/"
    #获取命令行参数
    sourcename = str(sys.argv[1])
    #取首字母
    first_letter = sourcename[0]
    #拼接url地址
    final_url = repo_url+"pool/main/"+first_letter+"/"+sourcename
    return final_url

def searchPackage():
    #访问链接地址
    try:
        response = urllib.request.urlopen(url_return())
        data = response.read().decode("utf-8")
        #print(data)
        #从获取的网页中把所有的html标签去除
        data = re.sub(r'\</.*\>',"",data)
        data= re.sub(r'\<.*\>',"",data)
        print(data)
        
        
    except Exception as error:
        print(error)

searchPackage()
