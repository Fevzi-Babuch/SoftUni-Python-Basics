
deposit = float(input())
period = int(input())
lihven_procent = float(input()) / 100

kraina_suma = deposit + period * ((deposit*lihven_procent)/12)

print(kraina_suma)
