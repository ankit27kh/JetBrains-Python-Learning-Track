N = int(input())

with open('applicant_list.txt', 'r') as f:
    data = f.readlines()
data = [d.split() for d in data]
for d in data:
    for i in range(2, 7):
        d[i] = float(d[i])


def sorting(data, count_b, count_c, count_e, count_m, count_p, pref, exam):
    """
    exam = 2 --> phy --> phy + math
    exam = 3 --> chem --> chem
    exam = 4 --> math --> math
    exam = 5 --> eng --> eng + math
    exam = 6 --> bio --> chem + phy
    """
    if exam == 2:
        data.sort(key=lambda x: (min(-(x[2] + x[4]) / 2, -x[6]), x[0], x[1]))
    if exam == 3:
        data.sort(key=lambda x: (min(-x[3], -x[6]), x[0], x[1]))
    if exam == 4:
        data.sort(key=lambda x: (min(-x[4], -x[6]), x[0], x[1]))
    if exam == 5:
        data.sort(key=lambda x: (min(-(x[5] + x[4]) / 2, -x[6]), x[0], x[1]))
    if exam == 6:
        data.sort(key=lambda x: (min(-(x[2] + x[3]) / 2, -x[6]), x[0], x[1]))
    for d in data:
        if 'Bio' in d[6 + pref] and exam == 6:
            if count_b < N:
                bio.append(d)
                count_b = count_b + 1
        elif 'Chem' in d[6 + pref] and exam == 3:
            if count_c < N:
                chem.append(d)
                count_c = count_c + 1
        elif 'Eng' in d[6 + pref] and exam == 5:
            if count_e < N:
                eng.append(d)
                count_e = count_e + 1
        elif 'Math' in d[6 + pref] and exam == 4:
            if count_m < N:
                math.append(d)
                count_m = count_m + 1
        elif 'Phy' in d[6 + pref] and exam == 2:
            if count_p < N:
                phy.append(d)
                count_p = count_p + 1
    for s in bio:
        if s in data:
            data.remove(s)
    for s in chem:
        if s in data:
            data.remove(s)
    for s in eng:
        if s in data:
            data.remove(s)
    for s in math:
        if s in data:
            data.remove(s)
    for s in phy:
        if s in data:
            data.remove(s)
    return data, count_b, count_c, count_e, count_m, count_p


bio = []
chem = []
eng = []
math = []
phy = []
count_b, count_c, count_e, count_m, count_p = 0, 0, 0, 0, 0
pref = 1

for exam in range(2, 7):
    data, count_b, count_c, count_e, count_m, count_p = sorting(data, count_b, count_c, count_e, count_m, count_p, pref, exam)
pref = pref + 1
for exam in range(2, 7):
    data, count_b, count_c, count_e, count_m, count_p = sorting(data, count_b, count_c, count_e, count_m, count_p, pref, exam)
pref = pref + 1
for exam in range(2, 7):
    data, count_b, count_c, count_e, count_m, count_p = sorting(data, count_b, count_c, count_e, count_m, count_p, pref, exam)

bio.sort(key=lambda x: (min(-(x[2] + x[3]) / 2, -x[6]), x[0], x[1]))
phy.sort(key=lambda x: (min(-(x[2] + x[4]) / 2, -x[6]), x[0], x[1]))
chem.sort(key=lambda x: (min(-x[3], -x[6]), x[0], x[1]))
math.sort(key=lambda x: (min(-x[4], -x[6]), x[0], x[1]))
eng.sort(key=lambda x: (min(-(x[5] + x[4]) / 2, -x[6]), x[0], x[1]))

with open('biotech.txt', 'w') as f:
    for s in bio:
        print(f"{s[0]} {s[1]} {max((s[2] + s[3]) / 2, s[6])}", file=f)
with open('chemistry.txt', 'w') as f:
    for s in chem:
        print(f"{s[0]} {s[1]} {max(s[3], s[6])}", file=f)
with open('engineering.txt', 'w') as f:
    for s in eng:
        print(f"{s[0]} {s[1]} {max((s[5] + s[4]) / 2, s[6])}", file=f)
with open('mathematics.txt', 'w') as f:
    for s in math:
        print(f"{s[0]} {s[1]} {max(s[4], s[6])}", file=f)
with open('physics.txt', 'w') as f:
    for s in phy:
        print(f"{s[0]} {s[1]} {max((s[2] + s[4]) / 2, s[6])}", file=f)
