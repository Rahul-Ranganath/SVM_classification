import random;
with open('testscores.txt', 'r') as myfile:
    data=myfile.read().split("\n");

goodlist = []
badlist = []
for i in data:
	temp = i.split(" ");
	if("Good" == temp[0] and temp[-1]!=''):
		goodlist.append(float(temp[-1]));
	elif(temp[-1]!=''):
		badlist.append(float(temp[-1]));

tp = 0;
tn = 0;
fp = 0;
fn = 0;
goodcount = 0;
badcount = 0;
# p =tp/tp + fp
# r = tp/tp+fn

while(True):
	k = random.random();
	if(goodcount < len(goodlist)):
		if(goodlist[goodcount]<20000):
			tp += 1;
		else:
			fp += 1;
		goodcount += 1;
		if(tn+fp > 0 and tp+fn > 0):
			
			print(((tp/(tp+fn))*100),100-((tn/(tn+fp))*100))
			# print(tp/(tp+fp),(tp/(tp+tn)))

	else:
		if(badcount < len(badlist)):
			if(badlist[badcount]>20000):
				tn += 1;
			else:
				fn += 1;
			badcount += 1;
			if(tn+fp > 0 and tp+fn > 0):
				print(((tp/(tp+fn))*100),100-((tn/(tn+fp))*100))
				# print(tp/(tp+fp),(tp/(tp+tn)))

	if(goodcount == len(goodlist) and badcount == len(badlist)):
		break;

print("true positives: ",tp,goodcount);
print("true negatives: ",tn,badcount);

print("good count: ",goodcount)
print("bad count: ",badcount)

print("average accuracy: ",(tp+tn)/(goodcount+badcount));