# Compact IntroToLoops.py using required constructs
geniuses = ["Luke","Tristan"]

for n in geniuses: print(n)
for i in range(len(geniuses)): print(i, geniuses[i])

i=0
while i<len(geniuses): print(geniuses[i]); i+=1

for n in geniuses:
	for c in n:
		if c==" ": continue
		print(c, end="")
	print()

for n in geniuses:
	if n.startswith("A"): continue
	print("Proc", n)
	if "Grace" in n: break

c=0
while True:
	print("loop",c)
	c+=1
	if c>1: break

