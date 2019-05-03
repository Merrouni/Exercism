colordict = [
            'black',
            'brown',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'violet',
            'grey',
            'white'
        ]

def color_code(color):
    return colordict.index(color)

def colors():
    return colordict

def value(colors):
    result = []
    for c in colors:
        result.append(color_code(c))
    return int(''.join(map(str, result)))
