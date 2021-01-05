from sys import argv

name, hours, rate, premium = argv
hours = int(hours)
rate = int(rate)
premium = int(premium)

wage = (hours * rate) + (hours * rate // 100) * 30
print(f'Заработная плата составила: {wage}')
