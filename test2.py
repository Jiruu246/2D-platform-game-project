value = 6

def createsmth():
    if __name__ == '__main__':
        print('something')

def createanother():
    print('another')

diction = {
    '3' : 'what',
    '1' : createsmth(),
    '2' : createanother(), 
}

print(diction['3'])