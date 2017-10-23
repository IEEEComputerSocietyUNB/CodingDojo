class ConvertTime:
    def __init__(self):
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

        self.hour_table = {k: v for (k,v) in zip(range(1,12), hours_names)}
        self.minute_table = {k: v for (k,v) in zip(range(0,61), minutes_names)}

    def time_with_utc(self, hour_minute):
        hm, utc = hour_minute.split(' ')
        hour, minute = list(map(int, hm.split(':')))

        if len(utc) == 3:
            return self.recv_time_correct_time(hm)
        else:
            if utc[3] == '+':
                hour = hour + int(utc[4])
            elif utc[3] == '-':
                hour = hour - int(utc[4])

            if hour < 1 or hour > 11:
                return 'ERROR'

            return self.recv_time_correct_time(str(hour)+':'+str(minute))

    def recv_time_correct_time(self, hour_minute):
        hour, minute = list(map(int, hour_minute.split(':')))

        if minute == 30:
            return self.hour_table[hour] + ' e meia'
        elif minute < 40:
            return self.recv_time_literal_time(hour_minute)
        else:
            minute_name = 60-minute
            hour_name = hour+1

            return self.minute_table[minute_name] + ' minutos para as ' + \
                    self.hour_table[hour_name]

    def recv_time_literal_time(self, hour_minute):
        hour, minute = list(map(int, hour_minute.split(':')))

        if hour < 1 or hour > 11 or minute < 0 or minute > 60:
            return 'ERROR'
        else:
            if hour == 1:
                result = self.hour_table[hour] + ' hora'
            else:
                result = self.hour_table[hour] + ' horas'

            if minute == 1:
                result = result + ' e ' + self.minute_table[minute] + ' minuto'
            elif minute != 0:
                result = result + ' e ' + self.minute_table[minute] + ' minutos'

        return result
