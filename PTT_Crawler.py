from PTTLibrary import PTT
ID = '你的ptt帳號'
Password = '你的ptt密碼'

PTTBot = PTT.Library()
PTTBot = PTT.Library(kickOtherLogin=False)

# 登入
ErrCode = PTTBot.login(ID, Password)


def PttCrawler(number,title):
    globalDoc=[]
    CrawPost=number
    
    def PostHandler(Post):
    globalDoc.append(Post.getContent())
    
    ErrCode, NewestIndex = PTTBot.getNewestIndex(Board=title)
    ErrCode, SuccessCount, DeleteCount = PTTBot.crawlBoard(title, PostHandler, StartIndex=NewestIndex - CrawPost + 1, EndIndex=NewestIndex)

    return(globalDoc)
