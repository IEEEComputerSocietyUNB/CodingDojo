def converter(horario):
    hour, minute = horario.split(':')
    hour_minute = list(map(int,[hour,minute]))

    numbers_table = {1: 'uma', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis'}
    decimal_table = {5: 'cinquenta'}
    minute_table = {0:'',
                    1: ' e um minuto',
                    56:' e cinquenta e seis minutos',
                    15: ' e quinze minutos',
                    30: ' e trinta minutos'}

    if hour_minute[0] < 1 or hour_minute[0] > 11 or hour_minute[1] < 0 or hour_minute[1] > 60:
        return 'error'
    else:
        if hour_minute[0] == 1:
            hora = ' hora'
        else:
            hora = ' horas'
        return numbers_table[hour_minute[0]] + hora + minute_table[hour_minute[1]]
