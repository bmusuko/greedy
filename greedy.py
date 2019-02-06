def count(x,y,i):
	if(i == 3):
		return(x+y)
	elif (i == 2):
		return(x-y)
	elif (i == 1):
		return(x*y)
	else:
		return(x/y)	

def convert(i):
	if(i == 0):
		return("/")
	elif(i == 1):
		return("*")
	elif(i == 2):
		return("-")
	else:
		return("+")

def main():
	FI = input("File Masukan : ")
	FO = input("File Keluaran : ")
	FInput = open(FI,"r")
	arr = []
	for line in FInput:
		arr.append(int(line))
	arr.sort()
	arrt = arr.copy()
	#print(arr)
	operator = 0
	arrO = []
	nilai = 0.0
	kurung = False
	for i in range(3):
		point = -100
		for j in range (4):
			kurungTemp = False
			x = count(arr[3-i],arr[2-i],j)
			temp = j-abs(24-x)+2 
			#print(x)
			if((j == 0 or j == 1) and (operator >1)):
				temp = temp - 1
				kurungTemp = True
			if ((temp)>point):
				point = temp
				nilai = x
				operator = j
				if(kurungTemp):
					kurung = True
		arr[2-i] = nilai
		#print(arr)
		arrO.append(operator)			
	#print(arrO)	
	#print(arr[0])
	#print(arrt)
	if(arrO[1] < 2 and arrO[0] >1):
		jawaban = "("+str(arrt[3])+convert(arrO[0])+str(arrt[2])+")"+convert(arrO[1])+str(arrt[1])+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)
	elif (arrO[2] < 2 and arrO[1] > 1):
		jawaban = "("+str(arrt[3])+convert(arrO[0])+str(arrt[2])+convert(arrO[1])+str(arrt[1])+")"+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)
	else :
		jawaban = str(arrt[3])+convert(arrO[0])+str(arrt[2])+convert(arrO[1])+str(arrt[1])+convert(arrO[2])+str(arrt[0])+" = "+str(nilai)
	print(jawaban)
	if (kurung):
		print("total point = "+str(-abs(24-arr[0])+sum(arrO)+6-1))
	else :
		print("total point = "+str(-abs(24-arr[0])+sum(arrO)+6))
	FOutput = open(FO,"w")
	FOutput.write(jawaban)
	FOutput.write("\n")

if __name__ == "__main__":
    main()