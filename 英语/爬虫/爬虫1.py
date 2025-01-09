# https://www.koolearn.com/
import httpx
from bs4 import BeautifulSoup


headers= {
    "Accept": "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3", 
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)"
    }
for urli in range(1, 3):
    url = "https://www.koolearn.com/dict/tag_1284_{}.html".format(urli)
    # print(url)

    res = httpx.get(url, headers=headers)
    res_text = (res.text.encode("utf-8"))
    soup = BeautifulSoup(res_text, "html.parser")
    word_text = soup.select("div.word-box")
    for word in word_text[0]:
        print(word.string, end="")


# import httpx
# from bs4 import BeautifulSoup


# headers= {
#     "Accept": "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3", 
#     "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)"
#     }


# for urli in range(1, 16): # range(x, y) 左闭右开区间, 从第x页到y-1页
#     url = "https://www.koolearn.com/dict/tag_1256_{}.html".format(urli)
#     # url = "https://www.koolearn.com/dict/tag_1269_1.html"
#     # print(url)

#     res = httpx.get(url, headers=headers)
#     res_text = (res.text.encode("utf-8"))
#     soup = BeautifulSoup(res_text, "html.parser")
#     word_text = soup.select("div.word-box")
#     for word in word_text[0]:
#         print(word.string, end="")