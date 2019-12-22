import re

#DPDA for a^(n).b^(n)
stack=['Z']
state=0
string=input('Enter input:')
i=0
flag=0
len_string=len(string)
for ch in string:
	flag=0
	print(ch)
	if ch=='a' and state==0:
		stack.append(ch)
		flag=1
	elif ch=='b' and stack[-1]=='a' and state==0:
		stack.pop()
		state=1
		flag=1
	elif ch=='b' and stack[-1]=='a' and state==1:
		stack.pop()
		flag=1
	print('State:q'+str(state))
	print('Stack:'+str(stack))
	i=i+1
# print('State:'+str(state)+'Stack:'+str(stack)+'i:'+str(i))
if state==1 and len(stack)==1 and stack[-1]=='Z' and i==len_string and flag==1:
	state=2

print('End')
if state==2:
	print('Accepted')
else:
	print('Not Accepted')
