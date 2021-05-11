count=1
range=int(input('enter range'))
while count <= range:
	rem = count % 2
	if rem == 0 :
		print(f'{count}is even')
	else:
		print(f'{count} is odd')
	count = count + 1 
print('thank you')

