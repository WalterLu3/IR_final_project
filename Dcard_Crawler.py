import requests, json
def DcardCrawler(number,title): ##輸入要爬的文章數目與板名（會依時間順序爬最新的） 回傳一個list，每個element裝一個文章的字串（不包含評論，如果有要抓評論再說）
    pages = int(number/30)
    header1={'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'}#要把身份設成browser不然不給爬
    Url="https://dcard.tw/_api/forums/"+title+"/posts?popular=false&" ##爬文章編號
    Url2="http://dcard.tw/_api/posts/" ##後面加編號 用編號爬文章
    docId = []##最後會裝文章編號
    allDocument=[]##最後會裝document
    for i in range(pages):##爬編號
        if (i==0):
            inputUrl=Url
        else:
            inputUrl=Url+"before="+str(docId[-1])
        a=requests.get(inputUrl,headers=header1)
        reqsjson = json.loads(a.text)
        for j in range(30):
            docId.append(reqsjson[j]["id"]) 
    inputUrl=Url+"before="+str(docId[-1])
    a=requests.get(inputUrl,headers=header1)
    reqsjson = json.loads(a.text)
    
    for i in range(0,number-30*pages):
        docId.append(reqsjson[i]["id"])
        
            
    for i in docId:##用上面的編號爬文章
        inputUrl=Url2+str(i)
        a=requests.get(inputUrl,headers=header1)
        reqsjson = json.loads(a.text)
        allDocument.append(reqsjson["content"])
        
    return(allDocument)
        
