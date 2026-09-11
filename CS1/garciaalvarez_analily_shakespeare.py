import random
list1 = ['bawdy', 'cackered',"frothy", 'gleeking','fribbling','ruttish', 'saucy', 'spleeny', 'venomed', 'coatish', 'weedy', 'yeasty']
list2 = ['beef-witted','crook-pated','dizzy-eyed','earth-vexing','fat-kidneyed','flap-mothed','guts-griping','milk-liveed','onion-eyed','tickle-brained', 'unchin-snoted', 'reeling-ripe']
list3 = ['bladder','bum-balley','clotpole','flap-dragon','flirt-gill','gudgeon', 'harpy', 'hedge-pig','jolthead', 'maggot pie', 'puttock', 'apple-john']

number = int(input("How many insults do you need? "))

for i in range(number):
    list1_index = random.randint(0, 12)
    list2_index = random.randint(0, 12)
    list3_index = random.randint(0, 12)
    print(f'Thou {list1[list1_index]} {list2[list2_index]} {list3[list3_index]}')
    