def converter(horario):
    hour, minute_e_utc = horario.split(':')
    minute, utc = minute_e_utc.split(' ')
    valor_do_utc = utc[3:]
    sinal_do_utc = valor_do_utc[1]

    if sinal_do_utc == '+':
        somar_na_hora = valor_do_utc[2] + hour

    else:
        subtrair_na_hora = hour - valor_do_utc[2]

    hour_minute = list(map(int,[hour,minute]))

    if hour_minute[0] < 1 or hour_minute[0] > 11 or hour_minute[1] < 0 or hour_minute[1] > 60:
        return 'error'
    else:
        if hour_minute[1] > 39:
            number = 60 - hour_minute[1]
            return numeroliteral(number) + ' minutos para as ' + numeroliteral(hour_minute[0] + 1)
        elif hour_minute[1] == 30:
            if hour_minute[0] == 1:
                return 'uma e meia'
            else:
                return numeroliteral(hour_minute[0]) + ' e meia'
        else:
            if hour_minute[0] == 1:
                hora = 'uma hora'
            else:
                hora = numeroliteral(hour_minute[0]) + ' horas'

            minutos = ''
            if hour_minute[1] == 1:
                minutos = ' e um minuto'
            elif hour_minute[1] > 1:
                minutos = ' e ' + numeroliteral(hour_minute[1]) + ' minutos'

            return hora + minutos

def numeroliteral(minuto):
    numbers_table = {
        0: '', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze',
        12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta'
    }

    if minuto < 20:
        return numbers_table[minuto]
    elif minuto < 40 and minuto%10 == 0:
        return numbers_table[(minuto)]
    elif minuto < 40 and minuto%10 != 0:
        return numbers_table[(minuto - minuto%10)] + ' e ' + numbers_table[minuto%10]
