# Напишите программу, удаляющую из текста все слова содержащие "абв".



text = 'хеллоу абвгдёшка почему ты абвкг..'

def d(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = d(text)
print(text)

