input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
sum = 0
if a >0:
    for i in range(1,a + 1):
        sum = sum + i
else:
    for i in range(a,2):
        sum = sum + i
b = str(sum)
output_data = open("output.txt","w")
output_data.write(b)
input_data.close()
output_data.close()