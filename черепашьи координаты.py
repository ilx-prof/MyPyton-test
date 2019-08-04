comand= [input().split() for i in range(int(input()))]
ai = [0,0]
for a in comand:
    if a[0] == "север":
         ai[1] = ai[1] + int(a[1])
    elif a[0] == "восток":
         ai[0] = ai[0] + int(a[1])
    elif a[0] == "запад":
         ai[0] = ai[0] - int(a[1])
    elif a[0] == "юг":
         ai[1] = ai[1] - int(a[1])
print (*ai)
         
"""
Интересное решение(небезопасное)

commands_sum = {'север': 0, 'юг': 0,
                'запад': 0, 'восток': 0}

for _ in range(int(input())):
    command, value = input().split()
    commands_sum[command] += int(value)

print(commands_sum['восток'] - commands_sum['запад'],
      commands_sum['север'] - commands_sum['юг'])

"""
