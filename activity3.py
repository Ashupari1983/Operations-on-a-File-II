f1 = open('b.txt','w')
f2 = open('a.txt','r')

lines_seen = set()

for i in f2.readlines():

    if i not in lines_seen:

        lines_seen.add(i)
        f1.write(i)

print(lines_seen)

f1.close()
f2.close()