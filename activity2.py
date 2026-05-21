file = open('a.py','x')
file.close()

import os

print("Checking for a.txt's existence...")

if os.path.exists('a.py'):
    print("The file is existing.")
    os.remove('a.py')
else:
    print('The file does not exist.')

f = open('b.py','w')
f.write("print('Hello World')")
f.close()


os.remove('folder/demo.txt')
os.rmdir('folder')