# IR_final_project

用法：
```
DcardCrawler(number,title) 
```
 number文章數量，title板名，會抓下"title"版名的最新number個數量。
 title名稱就去dcard網頁，隨便點一個板，就會看到他的英文網址，裡面有title。
 像是美妝：https://www.dcard.tw/f/makeup
 所以title就知道要輸入makeup
 假如說要抓前1000筆makeup板文章，dCardCrawl(1000,"makeup")

```
PTTCrawler(number,title) 
```
  用法與dcard相同，也要打英文板名，記得大小寫
  
  需要下載PTTLibrary package
```
pip install PTTLibrary
```
