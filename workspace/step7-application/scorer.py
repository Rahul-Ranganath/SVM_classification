def convolut(x1,x2):
	sum1 = 0;
	for i in range(len(x1)-1):
		sum1 += x1[i] * x2[i]
	return sum1

# w take from svm op
# take b from there


#take testg
#take testb

with open('svm_op.txt', 'r') as myfile:
    data=myfile.read().split("\n");

w = eval(data[0]);
b = eval(data[1]);

with open('reviewvectors.txt', 'r') as myfile:
    data=myfile.read().split("\n");

gtest = []
for i in range(len(data)):
	if(data[i] != ''):
		gtest.append(eval(data[i]))

	
for i in gtest:
	print(convolut(w,i)+b);
