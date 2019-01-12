from PTTLibrary import PTT
import dill
ID = '帳號'
Password = '密碼'

PTTBot = PTT.Library()
PTTBot = PTT.Library(kickOtherLogin=False)

# 登入
ErrCode = PTTBot.login(ID, Password)


def PttCrawler(number,title):
    globalDoc=[]
    CrawPost=number
    comment=[]
    title2=[]
    def PostHandler(Post):
        temp=[]
        for Push in Post.getPushList():
            temp.append(Push.getContent())
        globalDoc.append(Post.getContent())
        comment.append(temp)
        print(Post.getTitle())
        title2.append(Post.getTitle())
        
    ErrCode, NewestIndex = PTTBot.getNewestIndex(Board=title)
    ErrCode, SuccessCount, DeleteCount = PTTBot.crawlBoard(title, PostHandler, StartIndex=NewestIndex - CrawPost + 1, EndIndex=NewestIndex)
    
    while(len(globalDoc)<(number)):
        CrawPost=number-len(globalDoc)
        ErrCode, SuccessCount, DeleteCount = PTTBot.crawlBoard(title, PostHandler, StartIndex=NewestIndex - CrawPost + 1, EndIndex=NewestIndex)
    
    #comment留言
    #title2文章title
    #globalDoc文章內容
    with open (title+"_doc_Ptt",'wb') as file:
        dill.dump(globalDoc,file)
    with open (title+"_title_Ptt",'wb') as file:
        dill.dump(title2,file)
    with open (title+"_comment_Ptt",'wb') as file:
        dill.dump(comment,file)
    
    
    return(0)
