def verify(isbn):
    usableString = isbn.replace('-', '')
    if not isUsableISBN(usableString):
        return False
    result = 0
    for i in range(0,9):
        result += int(usableString[i])*(10-i)
        
    if usableString[-1] == 'X':
        result += 10
    else:
        result += int(usableString[-1])
        
    return result % 11 == 0

def isUsableISBN(usableString):
    return len(usableString) == 10 and usableString[:-1].isnumeric() and (usableString[-1].isdigit() or usableString[-1] == 'X')
