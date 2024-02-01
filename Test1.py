# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input('введите сумму депозита'))
# diposit = []
# diposit.append(int(per_cent['ТКБ']*money/100))
# diposit.append(int(per_cent['СКБ']*money/100))
# diposit.append(int(per_cent['ВТБ']*money/100))
# diposit.append(int(per_cent['СБЕР']*money/100))
# print(diposit)
# print('максимальная сумма по вкладу:', max(diposit))
# пусть a и b - переменные, которые мы хотим проверить

amount = 0
tickets = int(input("Введите количество билетов:\n"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:\n"))
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Проходите, детки, на конференцию!")
else:
    print("Стоимость Ваших билетов:", "%.2f" % tickets, "руб.")

if tickets > 3:
    discount = amount / 100 * 10
    print("Скидка составляет:", "%.2f" % discount, "руб.")
    print("К оплате:", "%.2f" % (amount -discount), "руб.")