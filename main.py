per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
su1 = float(input('Сумма вклада:'))

bank = list(per_cent.values())
a = float(bank[0])/100
b = float(bank[1])/100
c = float(bank[2])/100
d = float(bank[3])/100
a1 = su1 * a + su1
b1 = su1 * b + su1
c1 = su1 * c + su1
d1 = su1 * d + su1
print("Вклад + % за год в ТКБ", round(a1, 2), "руб")
print("Вклад + % за год в СКБ", round(b1, 2), "руб")
print("Вклад + % за год в ВТБ", round(c1, 2), "руб")
print("Вклад + % за год в СБЕР", round(d1, 2), "руб")

list_sm = [a1-su1, b1-su1, c1-su1, d1-su1]
print("Максимальный доход:", round(max(list_sm), 2), "руб")
max_key = max(per_cent, key=per_cent.get)
print("Будет получен в банке:", max_key)
