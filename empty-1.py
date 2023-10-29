print("Demon Slayers style breathing")
names = {
    'Abanai',
    'Mitsuri',
    'Rengoku',
    'Sanemi',
    'Shinobu',
    'Giuu',
    'Tokito',
    'Uzui'
}

power = {
    'Snake - style',
    'Love - style',
    'Fire - style',
    'Air - style',
    'Insects - style',
    'Water - style',
    'Fog - style',
    'Sound - style'
}

hashira_zip = zip(names, power)
conv_list = list(hashira_zip)

for j in conv_list:
    print(j, end='\n')
