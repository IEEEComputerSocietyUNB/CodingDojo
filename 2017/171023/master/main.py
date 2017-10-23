class ConvertTime:
    def recv_time(self, hour, minute):
        hours_names = ['uma', 'duas', 'três', 'quatro', 'cinco',
                        'seis', 'sete', 'oito', 'nove', 'dez',
                        'onze']

        base = ['um', 'dois'] + hours_names[2:-2]

        minutes_names =  base + hours_names[-2:] + ['doze',
                        'treze', 'quatorze', 'quinze', 'dezesseis',
                        'dezessete', 'dezoito', 'dezenove']

        twenty = lambda x : 'vinte e ' + x
        twenty_numbers = ['vinte'] + list(map(twenty, base))

        thirty = lambda x : 'trinta e ' + x
        thirty_numbers = ['trinta'] + list(map(thirty, base))

        forty = lambda x : 'quarenta e ' + x
        forty_numbers = ['quarenta'] + list(map(forty, base))

        fifty = lambda x : 'cinquenta e ' + x
        fifty_numbers = ['cinquenta'] + list(map(fifty, base))

        minutes_names = ['zero'] + minutes_names + twenty_numbers + \
                        thirty_numbers + forty_numbers + fifty_numbers

        hour_table = {k: v for (k,v) in zip(range(1,12), hours_names)}
        minute_table = {k: v for (k,v) in zip(range(0,61), minutes_names)}

        if hour < 1 or hour > 11 or minute < 0 or minute > 60:
            return 'ERROR'
        else:
            if hour == 1:
                result = hour_table[hour] + ' hora'
            else:
                result = hour_table[hour] + ' horas'

            if minute == 1:
                result = result + ' e ' + minute_table[minute] + ' minuto'
            elif minute != 0:
                result = result + ' e ' + minute_table[minute] + ' minutos'

        return result
