import re

print('Задание 1__Задание 1__Задание 1\n')
isu = 373331
print(isu % 6, isu % 4, isu % 7)

eyes = [':', ';', 'X', '8', '=', '\[']
noses = ['-', '<', '-{', '<{']
mouthes = ['\(', ')', 'O', '|', '\\', '/', 'P']
smile = '[<{('
print('My smile is:', smile, '\n')

pattern = fr"{eyes[isu % 6]}{noses[isu % 4]}{mouthes[isu % 7]}"

def number_of_occurrences(message, smile_s = pattern):
    print(f"Количество вхождений: {len(re.findall(smile_s, message))}, смайлика {smile} в сообщении: {message}", end='\nIs right result: ')
    return len(re.findall(smile_s, message))

test1 = f"Мой смайлик по варианту это - {smile}. А это второй - :-) - смайлик, который не мой."
test2 = f'{smile}{smile}{smile}'
test3 = 'X-O  ;<\\  =<{)  8-{|'
test4 = f'this is {smile} he is {smile} and soooo {smile} mean {smile} that {smile}.. ouhhh'
test5 = '[<{  <{(  [<)  [{) ' + smile

res1 = 1
res2 = 3
res3 = 0
res4 = 5
res5 = 1

print(res1 == number_of_occurrences(test1))
print(res2 == number_of_occurrences(test2))
print(res3 == number_of_occurrences(test3))
print(res4 == number_of_occurrences(test4))
print(res5 == number_of_occurrences(test5))


print('\n\nЗадание 2__Задание 2__Задание 2\n')

print(isu % 6, '\n')

glasn = r'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
sogl = r'бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ'

pattern = r'\w+[' + glasn + r']{2}\w*\s[' + glasn + r']*[' + sogl + r']?[' + glasn + r']*[' + sogl + r']?[' + glasn + r']*[' + sogl + r']?[' + glasn + r']*\s'

test1 = 'Кривошеее существо гуляет по парку'
res1 = 'гуляет'
res = re.findall(pattern, test1)
for i in res:
	print(re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0])
	print('Is right result:', re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0] == res1, '\n')

test2 = 'Где-то одинокая абоба ((('
res2 = 'одинокая'
res = re.findall(pattern, test2)
for i in res:
	print(re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0])
	print('Is right result:', re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0] == res2, '\n')

test3 = 'раздааача на спааавне'
res3 = 'раздааача'
res = re.findall(pattern, test3)
for i in res:
	print(re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0])
	print('Is right result:', re.findall(r'\w+[' + glasn + r']{2}\w*', i)[0] == res3, '\n')

test4 = 'инкапсуляция это не сокрытие'
res4 = 'инкапсуляция'
res = re.findall(pattern, test4)
for i in res:
	print(re.findall(r'\w+[аеёиоуыэюяАЕЁИОУЫЭЮЯ]{2}\w*', i)[0])
	print('Is right result:', re.findall(r'\w+[аеёиоуыэюяАЕЁИОУЫЭЮЯ]{2}\w*', i)[0] == res4, '\n')

test5 = 'я/мы животные это крутая песня'
res5 = 'животные'
res = re.findall(pattern, test5)
for i in res:
	print(re.findall(r'\w+[аеёиоуыэюяАЕЁИОУЫЭЮЯ]{2}\w*', i)[0])
	print('Is right result:', re.findall(r'\w+[аеёиоуыэюяАЕЁИОУЫЭЮЯ]{2}\w*', i)[0] == res5, '\n')


print('\n\nЗадание 3__Задание 3__Задание 3\n')

print(isu % 5, '\n')

glasn = [r'аА', r'еЕ', r'ёЁ', r'иИ', r'оО', r'уУ', r'ыЫ', r'эЭ', r'юЮ', r'яЯ']
sogl = r'бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ'

def Foo(text):
	ans = []
	ans += re.findall(r'\b[аАеЕёЁиИоОуУыЫэЭюЮяЯ]\b', text)
	for i in glasn:
		ans += re.findall(r'\b[' + sogl + i + r']{2,}\b', text)
	return ans

test1 = '''Классное слово – обороноспособность, 
которое должно идти после слов: трава 
и молоко.'''
test2 = '''Кроваво-черное ничто взмесило
Систему тел, спряженных в глуби тел,
Спряженных в глуби тем, там, в темноте
Спряженных тоже. Явственно до жути
Передо мной ударила из мути
Фонтана белоснежного струя
То был поток (мгновенно понял я)
Не наших атомов, и смысл всей сцены
Не нашим был. Ведь разум неизменно
Распознает подлог. в осоке — птицу,
В кривом сучке — личинку пяденицы,
А в капюшоне кобры — очерк крыл
Ночницы. Все же то, что заместил,
Перцептуально, белый мой фонтан,
Мог распознать лишь обитатель стран,
Куда забрел я на короткий миг.

Я тенью сойки был, нашедшей смерть
В лазури лживой, грянувшись о твердь
Стекла; я пухом был белесым - он
Парил, все в том же небе отражен.
А что за дивный вид, когда газон
Настолько снегопадом занесен,
Что кресла и кровать совсем вовне
Стоят - в снегу, в кристальной той стране.
Я тенью сойки был, нашедшей смерть,
С размаху, с лету грянувшись о твердь
С фальшивой перспективой.
У меня
Был мозг, пять чувств, - но простаком ни дня
Не перестал я быть. Играл во сне
С детьми, а утром вспоминалось мне,
Как мокрый был изрыт наискосок
Синусоидовалами песок
Следов велосипедных.
Как давно
Смерть дернула за струнку боли!

Что в тленье тихом верой греет нас
На воскресенье? Некий год? Иль час?
Кто счет ведет, в пути расставив вех?
Кого спасут - счастливцев или всех?
Вот - силлогизм: 'Да, все умрут; но я -
Отнюдь не все; и смерть - не для меня'.
Пространство - рой пчелиный. Время - песнь,
Жужжанье роя. Этот улей есть
Моя тюрьма. Но если б, не родясь,
Мы знали все про каждый икс, про грязь, -
То чем бы стала жизнь с тех самых пор?
Безумный, и тупой, и жалкий вздор!
Жизнь - это бред, что пишется во мгле'
В смоле труп муравья. А рядом - стрекоза:
Алмазный ларчик на сосне; глаза
Лягушечьи. Ошибся Лафонтен:
Певунья - жизнь; жевавший жвачку - тлен!'''
test3 = '''Я верю: я любим; для сердца нужно верить.
Нет, милая моя не может лицемерить;
Все непритворно в ней: желаний томный жар,
Стыдливость робкая, харит бесценный дар,
Нарядов и речей приятная небрежность,
И ласковых имен младенческая нежность.'''
test4 = '''Я вас любил: любовь еще, быть может,
В душе моей угасла не совсем;
Но пусть она вас больше не тревожит;
Я не хочу печалить вас ничем.
Я вас любил безмолвно, безнадежно,
То робостью, то ревностью томим;
Я вас любил так искренно, так нежно,
Как дай вам бог любимой быть другим.'''
test5 = '''Заслонили ветлы сиротливо
Косниками мертвые жилища.
Словно снег, белеется коливо —
На помин небесным птахам пища.

Тащат галки рис с могилок постный,
Вяжут нищие над сумками бечевки.
Причитают матери и крёстны,
Голосят невесты и золовки.

По камням, над толстым слоем пыли,
Вьется хмель, запутанный и клейкий.
Длинный поп в худой епитрахили
Подбирает черные копейки.

Под черед за скромным подаяньем
Ищут странницы отпетую могилу.
И поет дьячок за поминаньем:
“Раб усопших, Господи, помилуй”.'''

res1 = ['и', 'идти', 'слов', 'трава', 'слово', 'должно', 'молоко', 'обороноспособность']
res2 = ['я', 'и', 'А', 'я', 'Я', 'о', 'я', 'А', 'и', 'Я', 'о', 'У', 'я', 'а', 'я', 'и', 'и', 'и', 'А', 'на', 'за', 'за', 'На', 'Да', 'на', 'Не', 'Не', 'же', 'же', 'Не', 'не', 'не', 'не', 'из', 'ни', 'до', 'То', 'то', 'он', 'но', 'во', 'но', 'Но', 'То', 'во', 'Мы', 'бы', 'там', 'Как', 'Как', 'нас', 'час', 'тел', 'тел', 'тем', 'Все', 'все', 'сне', 'мне', 'вех', 'все', 'все', 'все', 'чем', 'тех', 'миг', 'вид', 'Иль', 'или', 'икс', 'что', 'мой', 'Мог', 'том', 'что', 'Что', 'той', 'Что', 'год', 'Кто', 'Вот', 'рой', 'про', 'про', 'пор', 'что', 'был', 'был', 'был', 'был', 'был', 'Был', 'был', 'дня', 'для', 'всей', 'Ведь', 'небе', 'счет', 'всех', 'есть', 'бред', 'мгле', 'тлен', 'лишь', 'мной', 'мозг', 'Кого', 'труп', 'крыл', 'быть', 'пять', 'стран', 'стала', 'глаза', 'греет', 'ведет', 'песнь', 'жизнь', 'Жизнь', 'жизнь', 'поток', 'вздор', 'умрут', 'смысл', 'грязь', 'смерть', 'твердь', 'смерть', 'твердь', 'Смерть', 'тленье', 'смерть', 'подлог', 'чувств', 'струнку']
res3 = ['Я', 'я', 'и', 'И', 'не', 'жар', 'дар', 'Нет', 'Все', 'ней', 'для', 'речей']
res4 = ['Я', 'Я', 'Я', 'Я', 'не', 'не', 'не', 'Но', 'То', 'то', 'вас', 'вас', 'вас', 'вас', 'вас', 'так', 'так', 'Как', 'дай', 'вам', 'еще', 'бог', 'быть', 'быть', 'пусть']
res5 = ['и', 'и', 'и', 'И', 'На', 'за', 'за', 'По', 'над', 'над', 'Раб', 'рис', 'поп', 'Под', 'снег', 'Тащат', 'хмель', 'черед', 'птахам', 'Словно']

res = sorted(Foo(test1), key=len)
for i in res:
	print(i)
print('Is right result:', res == res1, '\n\n')

res = sorted(Foo(test2), key=len)
for i in res:
	print(i)
print('Is right result:', res == res2, '\n\n') 

res = sorted(Foo(test3), key=len)
for i in res:
	print(i)
print('Is right result:', res == res3, '\n\n') 

res = sorted(Foo(test4), key=len)
for i in res:
	print(i)
print('Is right result:', res == res4, '\n\n') 

res = sorted(Foo(test5), key=len)
for i in res:
	print(i)
print('Is right result:', res == res5, '\n\n') 


def isPhoneNum(num):
	return  False if re.fullmatch(r'\+7\d{10}', num) == None else True

print(isPhoneNum('8888888839531'))