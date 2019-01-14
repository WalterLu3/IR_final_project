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
for i in range(0,10):
	print(Pttboard[i])
	file = open( Pttboard[i] + "_doc_Ptt_c",'rb')
	Ptt_doc = dill.load(file)
	file = open( Pttboard[i] + "_title_Ptt_c",'rb')
	Ptt_title = dill.load(file)
	file = open( Pttboard[i] + "_comment_Ptt_c",'rb')
	Ptt_comment = dill.load(file)
	content = []
	print("Start title doc content")
	for j in range(0,len(Ptt_doc)):
		content.extend(Ptt_title[j])
		content.extend(Ptt_doc[j])
	print("Start comment content")
	for j in range(0, len(Ptt_comment)):
		content.extend(Ptt_comment[j])
	print("End Content")
	V.extend(content)
	Cluster.append(content)
for i in range(0, 10):
	print(Dcardboard[i])
	file = open( Dcardboard[i] + "_doc_Dcard_c",'rb')
	Dcard_doc = dill.load(file)
	file = open( Dcardboard[i] + "_title_Dcard_c",'rb')
	Dcard_title = dill.load(file)
	file = open( Dcardboard[i] + "_comment_Dcard_c",'rb')
	Dcard_comment = dill.load(file)
	content = []
	print("Start title doc Content")
	for j in range(0, len(Dcard_doc)):
		content.extend(Dcard_title[j])
		content.extend(Dcard_doc[j])
	print("Start comment content")
	for j in range(0, len(Dcard_comment)):
		content.extend(Dcard_comment[j])
	print("End Content")
	V.extend(content)
	Cluster.append(content)

N = len(Cluster)
for i in range(0, 1):
	Cluster_set = list(set(Cluster[i]))
	scores = {word: tfidf(word, Cluster[i], V) for word in Cluster_set}
	sort_scores = sorted(scores.items(), key = lambda x:x[0])
	for j in range(0,10):
		print(sort_scores[j])
