# rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
# with open('5.4.duplicate.txt', 'w', encoding='utf-8') as dup:
#     with open('5.4.original.txt', 'r', encoding='utf-8') as orig:
#         dup.write(f'{str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in orig])}')

from googletrans import Translator

# pip install googletrans==3.1.0a0 - with a fix error 'NoneType' object has no attribute 'group'
# pip install googletrans==4.0.0rc1 - with a fix error 'NoneType' object has no attribute 'group'

with open('5.4.duplicate.txt', 'w', encoding='utf-8') as dup:
    with open('5.4.original.txt', 'r', encoding='utf-8') as orig:
        text = orig.read()
        translator = Translator()
        result = translator.translate(text, src='en', dest='ru')
        print(result.text)
        dup.write(f'{str([line.replace(line.split()[0], result.get(line.split()[0])) for line in orig])}')
