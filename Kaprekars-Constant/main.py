kap = list(input('Input a 4 digit number, using at least 2 different digits: '))

while len(kap) != 4:
    print('\nIt has to be 4 digits!')
    kap = list(input('Input a 4 digit number: '))

for i in (kap):
    a = (kap).count(i)
    while a > 2:
        print('There have to be at least 2 different digits!')
        kap = list(input('Input a 4 digit number: '))
        a = (kap).count(i)
        if a < 2:
            break

def kaprekar(x):
    if type(x) == int:
        kapmax = list(map(int, str(x)))
        kapmin = list(map(int, str(x)))
    else:
        kapmax = list(map(int, (x)))
        kapmin = list(map(int, (x)))
    kapmax.sort(reverse = True)
    kapmin.sort()
    kmax = int(''.join(map(str, kapmax)))
    kmin = int(''.join(map(str, kapmin)))
    print('{} - {} = '. format(kmax, kmin))
    print(kmax - kmin)
    global ans
    ans = kmax - kmin
    while ans != 6174:
        kaprekar(ans)

kaprekar(kap)
