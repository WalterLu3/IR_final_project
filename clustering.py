import dill,io,os,math
def n_containing(word, doc_count):
    return sum(1 for count in doc_count if word in count)
def tf(word, doc):
    return (doc.count(word)/len(doc))
def idf(word, doc_count):
    return math.log(N/ (1+n_containing(word,doc_count)))
def tfidf(word, doc, doc_count):
    return round(tf(word, doc)*idf(word, doc_count), 6)

Dcardboard = ['baseball','trending', 'entertainer', 'funny', 'girl', 'marvel', 'pokemon', 'relationship','vehicle', 'movie'] #看板名稱
Pttboard = ['Baseball', 'Gossiping', 'KoreaStar', 'StupidClown', 'WomenTalk', 'Marvel', 'PokemonGO', 'Boy-Girl', 'Biker', 'SuperBike'] #看板名稱
V = []
Cluster = []

f = open('stopwords.txt', encoding = 'utf8')
stopwords = [c for line in f for c in line.split()]

for i in range(0,10):
	print(Pttboard[i])
	file = open( Pttboard[i] + "_doc_Ptt_c",'rb')
	Ptt_doc = dill.load(file)
	file = open( Pttboard[i] + "_title_Ptt_c",'rb')
	Ptt_title = dill.load(file)
	file = open( Pttboard[i] + "_comment_Ptt_c",'rb')
	Ptt_comment = dill.load(file)
	content = []
	print("Start Content")
	for j in range(0,len(Ptt_doc)):
		title_removal = [c for c in Ptt_title[j] if c not in stopwords]
		doc_removal = [c for c in Ptt_doc[j] if c not in stopwords]
		content.extend(title_removal)
		content.extend(doc_removal)
	print("Start comment Content")
	for j in range(0, len(Ptt_comment)):
		com_removal = [c for c in Ptt_comment[j] if c not in stopwords]
		content.extend(com_removal)
	V.extend(content)
	Cluster.append(content)
	print("End Content")
print("Dcard")
for i in range(0, 10):
	print(Dcardboard[i])
	file = open( Dcardboard[i] + "_doc_Dcard_c",'rb')
	Dcard_doc = dill.load(file)
	file = open( Dcardboard[i] + "_title_Dcard_c",'rb')
	Dcard_title = dill.load(file)
	file = open( Dcardboard[i] + "_comment_Dcard_c",'rb')
	Dcard_comment = dill.load(file)
	content = []
	print("Start Content")
	for j in range(0, len(Dcard_doc)):
		title_removal = [c for c in Dcard_title[j] if c not in stopwords]
		doc_removal = [c for c in Dcard_doc[j] if c not in stopwords]
		content.extend(title_removal)
		content.extend(doc_removal)
	for j in range(0, len(Dcard_comment)):
		com_removal = [c for c in Dcard_comment[j] if c not in stopwords]
		content.extend(Dcard_comment[j])
	V.extend(content)
	Cluster.append(content)
	print("End Content")

N = len(Cluster)
for i in range(0, 1): #這裡選擇跑哪個版
	Cluster_set = list(set(Cluster[i]))
	print("set over")
	scores = {word: tfidf(word, Cluster[i], V) for word in Cluster_set}
	print("tfidf over")
	sort_scores = sorted(scores.items(), key = lambda x:x[0])
	if i > 9:
		num = i%10
		file = open( Dcardboard[num] + "_nfidf_stopwords.txt", 'a')
	else:
		file = open( Pttboard[i] + "_nfidf_stopwords.txt", 'a')
	for j in range(0,10):
		print(sort_scores[j])
		file.write( "{} {}\n".format(sort_scores[j][0], sort_scores[j][1]))
	file.close()