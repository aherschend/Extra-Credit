
dict = {"Father": 0, "God": 0, "Christ":0, "Spirit":0, "spirit": 0, "life" :0, "man" :0}


file = open('book of John text.txt','r')

john = file.read()

list = john.split()


for word in list:
    for key in dict:
        if key == word:
            dict[key] += 1


for word in dict:
    if word == 'Father':         
        print('Father:', dict['Father'])
    elif word == 'God':
        print('God:', dict['God'])
    elif word == 'Christ':
        print('Christ:', dict['Christ'])
    elif word == 'Spirit':
        print('Spriit:',dict['Spirit'])
    elif word == 'spirit':
        print('spirit:', dict['spirit'])
    elif word == 'life':
        print('life:', dict['life'])
    elif word == 'man':
        print('man:', dict['man'])