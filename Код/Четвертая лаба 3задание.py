dobicha = [90, 110, 120, 95, 115]
plan = 100
colvo_success_smen = 0
max_dobicha = dobicha[0]
vsego_dobili = 0

for i in range(len(dobicha)):
    vsego_dobili += dobicha[i]
    if dobicha[i] >= plan:
       colvo_success_smen += 1
    if dobicha[i] >= max_dobicha:
            max_dobicha = dobicha[i]

srednya_dobicha = vsego_dobili / len(dobicha)

print(f'Всего добыли {vsego_dobili}, средняя добыча {srednya_dobicha}, количество успешных смен {colvo_success_smen}, максимальная добыча {max_dobicha}')