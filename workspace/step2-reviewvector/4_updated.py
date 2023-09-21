import nltk;
import gensim;
import re;
import sys;

def add1(x1,x2):
	x = list()
	for i in range(len(x1)):
		x.append(x1[i]+x2[i])
	return x;

w2v_data = gensim.models.Word2Vec.load("../../data/datamodel.txt");

with open(sys.argv[1], 'r') as myfile:
    good_data=myfile.read()

with open(sys.argv[2], 'r') as myfile:
    bad_data=myfile.read()


g_data = good_data.split('\n')
b_data = bad_data.split('\n')

g_scores = list()
b_scores = list()

#for final training data in SVM
#good scores
countgoodmissed = 0;
for i in range(len(g_data)):
	#toks = nltk.word_tokenize(i)
	toks = re.findall(r'\w+',g_data[i])
	samplescore = list();
	for kk in range(50001):
		samplescore.append(0);
	for j in range(len(toks)):
		if(toks[j] in w2v_data.wv.vocab):
			samplescore = add1(samplescore,w2v_data.wv[toks[j]]) 
		else:
			countgoodmissed += 1;
	samplescore.append(1)
	g_scores.append(samplescore)
	print("good_i:",i);

#bad scores
countbadmissed = 0
for i in range(len(b_data)):
	toks = re.findall(r'\w+',b_data[i])
	samplescore = list();
	for kk in range(50001):
		samplescore.append(0);
	for j in range(len(toks)):
		if(toks[j] in w2v_data.wv.vocab):
			samplescore = add1(samplescore,w2v_data.wv[toks[j]]) 
		else:
			countbadmissed += 1;
	samplescore.append(-1)
	b_scores.append(samplescore)
	print("bad_i:",i);

print(len(g_scores))
print(len(b_scores))
print(countgoodmissed)
print(countbadmissed)

with open(sys.argv[3], 'w') as output:
	for i in g_scores:
		output.write(str(i)+'\n');

with open(sys.argv[4], 'w') as output:
	for i in b_scores:
		output.write(str(i)+'\n');

