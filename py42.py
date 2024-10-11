input_data = open('input.txt' , 'r')
data = input_data.read()
data = data.split()
N = int(data[0])
b = 1
if N == 1:
    out = 1
    output = open('output.txt', 'w')
    output.write(str(out))
elif N == 2:
    out =2
    output = open('output.txt', 'w')
    output.write(str(out))
elif N % 3 == 0:
    b = N // 3
    out = 3**b
elif N % 3 == 1:
    b = (N-2)//3
    out = 3**b*2*2
else:
    N % 3 == 2
    b = N // 3
    out = 3**b*2

output = open('output.txt', 'w')
output.write(str(out))

input_data.close()
output.close()
