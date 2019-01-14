# IR_final_project

用法：
```
DcardCrawler(number,title) 
```
 number文章數量，title板名，會抓下"title"版名的最新number個數量。
 title名稱就去dcard網頁，隨便點一個板，就會看到他的英文網址，裡面有title。
 像是美妝：https://www.dcard.tw/f/makeup
 所以title就知道要輸入makeup
 假如說要抓前1000筆makeup板文章，DcardCrawler(1000,"makeup")
 會直接在資料夾底下創出dill檔案

```
PTTCrawler(number,title) 
```
  用法與dcard相同，也要打英文板名，記得大小寫
  
  需要下載PTTLibrary package
```
pip install PTTLibrary
```

  clustering.py     
  V是全20000篇標題+文章+留言的集合     
  Cluster總共有20個，前面i = 0-9是ptt看板，後面10-19是Dcard看板，順序寫在code裡面。    
  配合stopwords.txt放在clean資料夾使用。    
  
