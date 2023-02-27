en = 'mnbvcxzlkjhgfdsapoiuytrewq'
ru = 'юбьтимсчяэждлорпавыфъхзщшгнекуцйё'

l_eng = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
l_russ = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

word = input('слово на русском или английском языке:')
if word[0].lower() in en:
    sum = 0
    for letter in word:
        for k, v in l_eng.items():
            if letter.upper() in v:
                sum += k
    print(f'стоимость слова на анлийском языке = {sum}')
else:
    if word[0].lower() in ru:
        sum = 0
        for letter in word:
            for k, v in l_russ.items():
                if letter.upper() in v:
                    sum += k
        print(f'стоимость слова на русском языке = {sum}')



























