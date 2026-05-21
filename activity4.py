with open('a.txt') as f1:
    data1 = f1.read()

with open('b.txt') as f2:
    data2 = f2.read()

data1 += '\n'
data1 += data2

print('Merging data...')

with open('merged.txt','w') as f:
    f.write(data1)

f.close()
f1.close()
f2.close()