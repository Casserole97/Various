F2 = int(input('Start the Sequence: '))
seq = int(input('How many terms?: '))
F1 = 0
x = 0
while x < seq:
    x+=1
    print(F1)
    f = (F1) + (F2)
    F1 = F2
    F2 = f
