with open('a.txt','w') as file:
    file.write("This is the text in the file. \nThis is line 2.\nThis is line 3.\nThis is line 4.")
file.close()

with open('a.txt','r') as file:
    data = file.readlines()
    for x in data:
        word = x.split()
        print(word)
file.close()