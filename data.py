myFile = open('data.txt', 'r')
lines = myFile.readlines()

def get(operation):
    if operation == 'usr':
        return lines[0][:-1]
    elif operation == 'pass':
        return lines[1][:-1]
