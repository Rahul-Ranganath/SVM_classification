import nltk
import gensim
import re

with open('../../data/intermediate/gooddata.txt', 'r') as myfile:
    good_data=myfile.read()

with open('../../data/intermediate/baddata.txt', 'r') as myfile:
    bad_data=myfile.read()


g_data = good_data.split('\n')
b_data = bad_data.split('\n')

data = g_data + b_data;
# #print(ls);
# gooddata = []
# baddata = []
# for j in ls:
# 	if(j[:3] == "__1"):
# 		baddata.append(j[3:])
# 	else:
# 		gooddata.append(j[3:])

#print(gooddata)
#print(baddata)

# print(len(gooddata));
# print(len(baddata))

data_tokens = list();

for i in range(len(data)):
	data_tokens.append(re.findall(r'\w+',data[i]))

print("Done tokenizing with data")

print("Start w2vec")


w2v_data = gensim.models.Word2Vec(data_tokens, size=len(data_tokens))
print("Done with data")

print("data: ",w2v_data)
for word, vocab_obj in w2v_data.wv.vocab.items():
	print(word,w2v_data.wv[word])

w2v_data.save("../../data/intermediate/datamodel.txt");