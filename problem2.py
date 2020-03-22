s=input('ENTER THE FIRST DNA SEQUENCE:')
t=input('ENTER THE SECOND DNA SEQUENCE:')
mismatch=0
for i in range(len(s)):
    if s[i]!= t[i]:
	    mismatch+=1

		
print(mismatch)
