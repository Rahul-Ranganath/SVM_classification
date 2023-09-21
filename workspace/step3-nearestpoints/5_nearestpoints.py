import numpy as np
import scipy.spatial.distance as dist

with open('../../data/intermediate/goodresults.txt', 'r') as myfile:
    good_data=myfile.read()

with open('../../data/intermediate/badresults.txt', 'r') as myfile:
    bad_data=myfile.read()

good_vectors = good_data.split("\n");
bad_vectors = bad_data.split("\n");

good_list = []
bad_list = []

# print(good_vectors)
for i in good_vectors:
	if(i != ''):
		good_list.append(eval(i));

for i in bad_vectors:
	if(i != ''):
		bad_list.append(eval(i));


# i,j = np .where(arr == arr.min())

# print(good_list[324])

# print(bad_list[279])

# arr = dist.cdist(good_list[324],bad_list[279], "euclidean")

# print(arr)

g_value ="";

for i in range(len(good_list[324])):
	g_value = g_value + str(good_list[324][i]) + " ";

g_value = g_value + "1";

b_value = "";

for i in range(len(bad_list[279])):
	b_value = b_value + str(bad_list[279][i]) + " ";

b_value = b_value + "-1";

with open('../../data/intermediate/svm_ip.txt', 'w') as output:
	output.write(g_value+'\n');
	output.write(b_value+'\n');
