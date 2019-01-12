import requests, json,dill
def DcardCrawler(number,title): ##輸入要爬的文章數目與板名（會依時間順序爬最新的） 回傳一個list，每個element裝一個文章的字串（不包含評論，如果有要抓評論再說）
    pages = int(number/30)
    header1={'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1'}#要把身份設成browser不然不給爬
    Url="https://dcard.tw/_api/forums/"+title+"/posts?popular=false&" ##爬文章編號
    Url2="http://dcard.tw/_api/posts/" ##後面加編號 用編號爬文章
    docId = []##最後會裝文章編號
    allDocument=[]##最後會裝document
    comment=[]
    title2=[]
    for i in range(pages):##爬編號
        if (i==0):
            inputUrl=Url
        else:
            inputUrl=Url+"before="+str(docId[-1])
        a=requests.get(inputUrl,headers=header1)
        reqsjson = json.loads(a.text)
        for j in range(30):
            docId.append(reqsjson[j]["id"]) 
    
    if pages>1 :
        inputUrl=Url+"before="+str(docId[-1])
        a=requests.get(inputUrl,headers=header1)
        reqsjson = json.loads(a.text)
        for i in range(0,number-30*pages):
            docId.append(reqsjson[i]["id"])
    else:
        for i in range(0,number):
            a=requests.get(Url,headers=header1)
            reqsjson = json.loads(a.text)
            docId.append(reqsjson[i]["id"])
        
            
    for i in docId:##用上面的編號爬文章
        inputUrl=Url2+str(i)
        a=requests.get(inputUrl,headers=header1)
        reqsjson = json.loads(a.text)
        allDocument.append(reqsjson["content"])
        title2.append(reqsjson["title"])

        inputUrl2 = "http://dcard.tw/_api/posts/"+str(i)+"/comments"
        b=requests.get(inputUrl2,headers=header1)
        reqsjson2 = json.loads(b.text)
        temp=[]
        for j in reqsjson2:
            if 'content' in j:
                temp.append(j['content'])
        comment.append(temp)
    #title2存文章題目
    #allDocument存文章內容
    #comment存文章回覆
    
    with open (title+"_doc_Dcard",'wb') as file:
        dill.dump(allDocument,file)
    with open (title+"_title_Dcard",'wb') as file:
        dill.dump(title2,file)
    with open (title+"_comment_Dcard",'wb') as file:
        dill.dump(comment,file)
        
    return(allDocument)
