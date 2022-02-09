for row in range(10):
    for col in range(0,10-row):
    
        print(col,end=" ")
    
    print('\r')


def pypart(n):
	myList = []
	for i in range(0,n+1):
		myList.append(str(i)*i)
	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)


def contalpha(n):
	
	# initializing value corresponding to 'A'
	# ASCII value
    num = 65

	# outer loop to handle number of rows
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
		
			# printing char value
            print(ch, end=" ")
		
			# incrementing at each column
            num = num +1
	
	
		# ending line after each row
        print("\r")

# Driver code
n = 5
contalpha(n)

