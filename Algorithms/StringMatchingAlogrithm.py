def search(pat, txt):
	M = len(pat)
	N = len(txt)
	for i in range(N - M + 1):
		j=0
		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1
		if (j == M):
			print("Pattern found at index ", i)
# Driver's Code
tn=int(input("Enter no. of text"))
txt=[]
for i in range(0,tn):
	ele=str(input("Enter Text Elements"))
	txt.append(ele)
pat=[]
pn=int(input("Enter no. of pattern"))
for j in range(0,pn):
	el=str(input("Enter pattern Elements"))
	pat.append(el)
# Function call
search(pat, txt)