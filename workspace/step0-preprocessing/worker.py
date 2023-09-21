countergood = 1
counterbad = 1
countergoodtest = 1
counterbadtest = 1

# determining the label with record[:3] since label is removed in line 15, the rest of the line is the review itself
def fn(record, goodcounter, badcounter, goodarr, badarr, maxnum):
	if(record[:3] == "__1" and badcounter<=maxnum):
		badarr.append(record[3:])
		badcounter += 1;
	elif(goodcounter<=maxnum):
		goodarr.append(record[3:])
		goodcounter += 1
	return (badcounter,goodcounter)

#training data
with open('../../data/test.ft.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
ls = data.split("__label")

#testing data
with open('../../data/test.ft.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
ls2 = data.split("__label")
#print(ls);
gooddata = []
baddata = []
gooddatatest = []
baddatatest = []

#training data
for j in ls:
	counterbad, countergood = fn(j, countergood, counterbad, gooddata, baddata, 25000) # 25000 training from good and bad -> makes it 50000 reviews totally for training
	if(countergood>25000 and counterbad>25000):
		break;

#testing data
for j in ls2:
	counterbadtest, countergoodtest = fn(j, countergoodtest, counterbadtest, gooddatatest, baddatatest, 500)
	if(countergoodtest>500 and counterbadtest>500):
		break;


with open('../../data/intermediate/gooddata.txt', 'w') as output:
	for j in gooddata:
		output.write(j+"\n");
	print("gooddata.txt done: ",len(gooddata));

with open('../../data/intermediate/baddata.txt', 'w') as output:
	for j in baddata:
		output.write(j+"\n");
	print("baddata.txt done: ",len(baddata));

with open('../../data/intermediate/goodtestdata.txt', 'w') as output:
	for j in gooddatatest:
		output.write(j+"\n");
	print("goodtestdata.txt done: ",len(gooddatatest));

with open('../../data/intermediate/badtestdata.txt', 'w') as output:
	for j in baddatatest:
		output.write(j+"\n");
	print("badtestdata.txt done: ",len(baddatatest));

