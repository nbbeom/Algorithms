data = input().split()

MS = list(set(data[0:2]))
TK = list(set(data[2:]))

dic = {
    'R':'P',
    'P':'S',
    'S':'R'
}


if len(MS) == 1 and dic[MS[0]] in TK:
        print("TK")
elif len(TK) == 1and dic[TK[0]] in MS:
        print("MS")
else:
    print("?")
