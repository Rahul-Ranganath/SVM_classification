from sympy import *;


#convolution i.e xi*xj
def convolut(x1,x2):
	sum1 = 0;
	for i in range(len(x1)-1):
		sum1 += x1[i] * x2[i]
	return sum1

def conv_to_list(hello):
	busy = []
	for i in hello.keys():
		busy.append(hello[i])
	return busy

def mod(x):
	m = 0 
	for i in x:
		m += i*i
	m = m**(1/2)
	return m

def ret_tuple(hello):
	eg=[]
	
	for i in range(len(hello)-1):
		eg.append(hello[i])
	eg=tuple(eg)
	return eg

#equation 1
def fun(points):
	num = len(points);
	ls = []
	for j in range(num):
		ls.append(Symbol("alpha"+str(j+1)))
	print("ls:",ls);
	equation = "";
	for p in range(len(ls)):
		if(p!=len(ls)-1):
			equation += str(ls[p])+"*"+str(points[p][-1])+" + ";
		else:
			equation += str(ls[p])+"*"+str(points[p][-1]);
	print("alphai yi question:", equation);
	equation1 = solve(equation,ls[-1]);
	print("solved: ",equation1)
	return equation1,ls;

#equation 2
def dual(points):
	equation1,ls = fun(points);
	equation2 = Symbol("equation2");
	ls[-1] = equation1[0]
	# print('here')
	# print(ls[-1])
	equation2 = 0
	for i in range(len(ls)):
		equation2 += ls[i];
	print("equation2: ", equation2);

	# print(equation2);
	eq22 = Symbol("eq22");
	alphascore = Symbol("alphascore");
	x_score = Symbol("x_score");
	y_score = Symbol("y_score");
	eq22 = 0;
	for i in range(len(ls)):
		for j in range(len(ls)):
			x_score = 0;
			y_score = 0;
			alphascore = 0;
			x_score = convolut(points[i],points[j]);
			y_score = points[i][-1] * points[j][-1];
			alphascore = ls[i] * ls[j];
			# print(x_score,y_score,alphascore)
			# print()
			eq22 += alphascore * x_score * y_score
	eq22 /=2
	# print(eq22)
	final_eq2 = Symbol("final_eq2")
	final_eq2 = 0
	final_eq2  = equation2 - eq22
	# print(type(final_eq2))
	print("equation")
	print(final_eq2)
	# print(type(ls[0]));
	print()
	final_eqns = []
	for i in range(len(ls)-1):
		# print()
		# print(diff(final_eq2,ls[i]))
		# print()
		final_eqns.append( diff(final_eq2,ls[i]))
	# 	print(final_eqns[i])
	# 	print()
	# print (final_eqns)

	# lis_of_equations = conv_to_list(final_eqns)
	
	eg = ret_tuple(ls)
	print("eg:", eg)
	
	final_values = dict()
	final_values1 = list(linsolve(final_eqns,eg))
	print ("lis_of_equations:", final_eqns)
	print("final_values:", final_values1)

	for i in range(len(final_values1[0])):
		final_values[ls[i]] = final_values1[0][i]

	print("final_values:", final_values)
	for j in range(len(ls)):
		for k in final_values.keys():
			ls[j]= ls[j].subs(k,final_values[k])

	print(ls);

	alpha1 = ls[0]
	alpha2 = ls[1];
	print("alpha1: ",alpha1);
	print("alpha2: ",alpha2);
	return alpha1,alpha2;
	# equation3(points);

def equation3(points):
	alphas = dual(points);
	pr = list();
	k = list();
	for i in range(len(points)):
		k.append(list(points[i]));
		pr.append(list(points[i]));

	for i in range(len(pr)):
		for j in range(len(pr[i])):
			pr[i][j] = 0;

	for i in range(len(points)):
		mul = alphas[i] * points[i][-1]
		for j in range(len(k)):
			k[i][j] *= mul;
	
	for i in range(len(k)):
		for j in range(len(k[i])-1):
			pr[0][j] += k[i][j]

	# print("k:",k)
	# print(pr[0]) 
	final_w = pr[0]
	# print("w:" , final_w)	

	#calculating b and whole formula
	x1 = list(points[0])
	x2 = list(points[1])
	# print("x1: ",x1,"x2: ",x2)
	# print("hello:", convolut(final_w, x2))
	b = -(convolut(final_w,x1) + convolut(final_w,x2))/2
	# print("b: ", b)
	return final_w,b


with open("../../data/intermediate/svm_ip.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
ls = []
for j in content:
	k = j.split();
	for p in range(len(k)):
		k[p] = float(k[p]);
	ls.append(tuple(k));
print(ls);

w,b = equation3(ls);
print("equation: ")
print(w[:-2],"x + ",b);

with open('../../data/intermediate/svm_op.txt', 'w') as output:
	output.write(str(w[:-2]) + "\n") #Printing w ->  output.write("w= "+ str(w[:-2]) + "\n")
	output.write(str(b) + "\n") #Printing b      ->  output.write("b= "+ str(b) + "\n")
 

m = mod(w)
m = 2/m
print("margin: ",m)
