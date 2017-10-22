class ConvertTime:
    def recv_time(self, hour, minute):
        if hour < 1 or hour > 11 or minute < 0 or minute > 60:
            return 'ERROR'
        else:
            result = str(hour) + str(minute)

        return result
