with open('reviewscores.txt', 'r') as myfile:
    data=myfile.read().split("\n");

goodlist = []
for i in data:
	temp = i.split(" ");
	if(temp[-1]!=''):
		goodlist.append(float(temp[-1]));
tp = 0;
tn = 0

for j in goodlist:
	if(j<40000):
		tp += 1;
	else:
		tn += 1;

print(tp);
print(tn);

if(tp > tn):
	print("GOOD");
else:
	print("BAD");