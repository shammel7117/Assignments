#Stephen Hammel
#Splitting string values using 'custom' formatting

with open("Python samples/iris.csv") as f:
  for line in f:
    line = line.replace(',', ' ')
    line = line.rstrip()
    print(line[:16].strip())
