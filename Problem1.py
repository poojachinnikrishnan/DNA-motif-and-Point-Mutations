s=input('ENTER THE DNA SEQUENCE:')
t=input('ENTER THE DNA MOTIF:')
for i in range(len(s)):
	if s[i:i+len(t)]==t:
		print(i+1, end =" ")
