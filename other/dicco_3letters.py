def freq_month(obj):
    if obj is None or obj is []:
        return
    months = {'jan': 0,
              'feb': 0,
              'mar': 0,
              'apr': 0,
              'may': 0,
              'jun': 0,
              'jul': 0,
              'aug': 0,
              'sep': 0,
              'oct': 0,
              'nov': 0,
              'dec': 0,
             }

    for i in range(0, len(obj)):
        for j in months:
            if obj[i] is j:
                months[j] += 1
                break
    return months

in_array = ['apr','dec','aug', 'mar', 'jul', 'jul']
print freq_month(in_array)
print sorted(freq_month(in_array))
