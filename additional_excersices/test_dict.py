pets = {
    'dog': 'wuffy',
    'cat': 'mauzi',
    'rabbit': ['jumpy', 'diggy']
}

name = 'jumpy'

for key,value in pets.items():
    # print(key)
    if value == name or name in value:
        print(f'{name} is a {key}')


