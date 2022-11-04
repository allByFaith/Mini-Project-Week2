import csv

# Create an empty for reading the orders
myOrderList = []

# With the “With” statement (File Context Manager), you get better syntax and 
# exceptions handling.  The with statement simplifies exception handling by encapsulating 
# common preparation and cleanup tasks.  In addition, it will automatically close 
# the file. With statement provides a way for ensuring that a clean-up is always used.
# i.e. We didn’t have to write “file.close()”. That will automatically be called.
with open("orderTrans.csv", 'r') as readFile:
    csvreader = csv.reader(readFile)
    header = next(csvreader)
    for readRow in csvreader:
        myOrderList.append(readRow)

print(header)
print(myOrderList)