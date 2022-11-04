# load csv module
import csv

# Writing to CSV files using the DictWriter class
# If each row of the CSV file is a dictionary, 
# you can use the DictWriter class of the csv module 
# to write the dictionary to the CSV file.

# define a dictionary with key value pairs
# order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]

myOrderList = [{'customer_name':'Nishu','customer_address':'address in Manchester','customer_phone':'601','status':'processing'},
                {'customer_name':'Megha','customer_address':'address 1 for Megha','customer_phone':'602','status':'processing'},
                {'customer_name':'Zach', 'customer_address':'.address near the city center','customer_phone':'603','status':'processing'},
                {'customer_name':'Rachel','customer_address':'Bolton of UK','customer_phone':'604','status':'processing'},
                {'customer_name':'Rachal','customer_address':'The main office of Generation','customer_phone':'605','status':'processing'},
                {'customer_name':'Tom','customer_address':'Not specified','customer_phone':'606','status':'processing'}]

# myOrderList = {}

# below field must match with the keys in myOrderList
fields = ['customer_name','customer_address','customer_phone','status']

# print(myOrderList)

orderFile = "orderTrans.csv"

# With the “With” statement (File Context Manager), you get better syntax and 
# exceptions handling.  The with statement simplifies exception handling by encapsulating 
# common preparation and cleanup tasks.  In addition, it will automatically close 
# the file. With statement provides a way for ensuring that a clean-up is always used.
# i.e. We didn’t have to write “file.close()”. That will automatically be called.

# with open(orderFile, 'a+') as csvFile:
#     writer = csv.DictWriter(csvFile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(myOrderList)

# myOrderList_1 = [{'customer_name':'John','customer_address':'address in the north of Manchester','customer_phone':'609','status':'Out-for-Delivery'}]

with open(orderFile, 'a+') as csvFile:
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    if (len(myOrderList)==0):
        writer.writeheader()
    
    writer.writerows(myOrderList)
    # writer.writerows(myOrderList_1)