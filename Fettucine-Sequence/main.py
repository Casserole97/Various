F = int(input('Start the Sequence: '))
seq = int(input('How many terms?: '))
x = 0
while x < seq:
    x+=1
    f = (F*x-1) + (F*x-2)
    print(f)
    F = f