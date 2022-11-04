# This is the mini-project
# File Name     : listStorage.py
# Date          : 28 Oct 2022
# Developer     : Samuel KO
# Description   : Create a list for app use, a list of methods can be called for file handling
#               : 1) openFileToWrite(inItem)
#               : 2) openFileToRead()
#               : 3) openFileToUpdate(inItem, updateItem, inAction)
#               : 4) closeFile(fileHandle)
#
# e.g. myList = ["Coca Cola Classic","Coke Zero","Pepsi Cola","Diet Pepsi","Sprite","Fanta","Dr. Peper"]
import traceback

# openFileToRead() for reading a file
def openFileToWrite(inItem):
    try:
        # traceback.print_exc()
        fileHandle = open("/data/product.txt", "a+")
        inItem = inItem + "\n"
        fileHandle.write(inItem)
    except:
        traceback.print_exc()

# openFileToWrite() for writing a file
def openFileToRead():
    # Create a temperary list for use
    tempList = []
    try:
        fileHandle = open("../data/product.txt", "r")  # Open product.txt which under data/ directory for reading 
        print("Open file to read the product list :-")
        tempFileObj = fileHandle.readlines()
        for readItem in tempFileObj:
            if('\n' in readItem):
                readItem = readItem[:-1]
            tempList.append(readItem)
        print(tempList)
    except:
        fileHandle = open("../data/product.txt", "x")
        print("Create file")

    return tempList

def openFileToUpdate(inItem, updatedItem, inAction):
    import os

    # use two value for inAction : 1) u - update item
    #                            : 2) d - delete item

    fileHandle = open("../data/temp.txt", "x")
    try:
        with open("../data/product.txt", "r") as inputW:
            with (open("../data/temp.txt", "a")) as outputW:
                for readItem in inputW:
                    if((readItem.strip() != inItem)):
                       outputW.write(readItem)
                    else:
                        if(inAction == 'd'):
                            pass
                        elif(inAction == 'u'):
                            outputW.write(updatedItem + "\n")

        os.replace('../data/temp.txt', 'data/product.txt')                
    except:
        traceback.print_exc()

def closeFile(inFileHandle):
    inFileHandle.close()

# Below code use for self testing....
# def main():
#     f = openFileToRead()
#     # print(f)
#     # item = "New Item"
#     # f = openFileToWrite(item)
    
#     finalStatus = closeFile(f)

# main()
