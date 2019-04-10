# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    if len(ticket_number) != 6:
        return ("Введен некорректный номер билета")
    else:
        sum1 = sum(int(x) for x in ticket_number[0:3])
        sum2 = sum(int(x) for x in ticket_number[3:6])
        if sum1 == sum2:
            return ("Счастливый билет")
        else:
            return ("Билет не счастливый")


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
