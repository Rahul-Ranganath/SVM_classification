from matplotlib import pyplot as plt

with open('statistics.txt', 'r') as myfile:
    data=myfile.read().split("\n");
x = []
y = []
temp = ''
for i in data:
	if(i != ''):
		temp = i.split(" ");
		x.append(float(temp[0]))
		y.append(float(temp[1]))

plt.plot(y,x)
plt.xlabel("False positive rate");
plt.ylabel("True positive rate");
plt.show();
