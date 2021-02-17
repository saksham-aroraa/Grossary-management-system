import pickle
import random as r
import os
import time as t

#Display All Products
def disp_all():
    print(40*"~~~~","\n\n")
    print("                             All Products\n")
    print(40*"~~~~","\n")
    try:
        file=open("prodlist.dat","rb")
        print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
        print(20*"~~~~")
        prod = pickle.load(file)
        for x in prod:
            print("%-4s"%x[0],"%-7s"%x[1],"%-35s"%x[2],"%-12s"%x[3],"%-8s"%x[4],"%-5s"%x[5])
        file.close()
    except EOFError:
        file.close()
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

#search Product
def disp_prod():
    print(40*"~~~~","\n\n")
    print("              Search By Name\n")
    print(40*"~~~~","\n")
    try:
        pl=input("Type Product Name : ")
        prod = []
        file=open("prodlist.dat","rb")
        data = pickle.load(file)
        for i in data:
            prod.append(i)
        print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
        for i in prod:
            if i[2] == pl:
                print("%-4s"%i[0],"%-7s"%i[1],"%-35s"%i[2],"%-12s"%i[3],"%-8s"%i[4],"%-5s"%i[5])
        file.close()
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")        
    except IOError:
        print("File Not Found")

def seller():
    #main
    #Add Product
    def new_prod():
        print(40*"~~~~","\n\n")
        print("              Add Products\n")
        print(40*"~~~~","\n")
        try:
            prod = []
            file=open("prodlist.dat","rb")
            data = pickle.load(file)
            for i in data:
                prod.append(i)
            file.close()
            file=open("prodlist.dat","wb")
            while True:
                data=[]
                data.append(r.randint(0,999))
                data.append(r.randint(10000,99999))
                print("Your Serial No. is : ",data[0]) 
                print("Product No. is : ",data[1]) 
                data.append(input("Type Product Name : "))
                data.append(input("Type Product Type : "))
                data.append(int(input("Type Product Quantity : ")))
                data.append(int(input("Type Product Price : ")))
                data.append([])
                prod.append(data)
                x = input("Do you want to save more records? (y/n)")
                if x == "n":
                    break
            pickle.dump(prod,file)
            file.close()
            print("Product Added Successfully")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except EOFError:
            prod = []
            file=open("prodlist.dat","wb")
            while True:
                data=[]
                data.append(r.randint(0,999))
                data.append(r.randint(10000,99999))
                print("Your Serial No. is : ",data[0]) 
                print("Product No. is : ",data[1]) 
                data.append(input("Type Product Name : "))
                data.append(input("Type Product Type : "))
                data.append(int(input("Type Product Quantity : ")))
                data.append(int(input("Type Product Price : ")))
                data.append([])
                prod.append(data)
                x = input("Do you want to save more records? (y/n)")
                if x == "n":
                    break
            pickle.dump(prod,file)
            file.close()
            print("Product Added Successfully")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except:
            pass

    def remove_prod():
        z=0
        try:
            #reading the data from the file
            prod = []
            temp = []
            file=open("prodlist.dat","rb")
            prod = pickle.load(file)
            file.close()
            n=int(input("Type Serial No. Or Product No. of the item to be removed: "))
            file=open("prodlist.dat","wb")
            #checking whether given number is correct or not
            for x in prod:
                if(x[0] == n or x[1] == n):
                    z = 1
            if z == 0:
                print("Product not found, enter a valid number")
            else:
                for x in prod:
                    if x[0] == n or x[1] == n:
                        print("Product Found:")
                        print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
                        print("%-4s"%x[0],"%-7s"%x[1],"%-35s"%x[2],"%-12s"%x[3],"%-8s"%x[4],"%-5s"%x[5])
                    else:
                        temp.append(x)
                prod = temp
                pickle.dump(prod,file)      
                print("\n\nProduct Removed Successfuly")
            file.close()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except IOError:
            print("File Not Found")
        input("Press Enter To Continue...")

#Remove All Products
    def remove():
        print(40*"~~~~","\n\n")
        print("        Remove All Products")
        print(40*"~~~~","\n")
        try:
            a=input("Do You Really Want To Remove All Products...(y/n): ")
            if(a=='y'):
                file = open("prodlist.dat","wb")
                prod = []
                pickle.dump(prod, file)
                print("All Products Removed Successfuly")
            else:        
                print("Removing All Products Unsuccessful")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except:
            print("Sorry, Data could not be deleted.")
            pass

#All Buyers
    def disp_buyer():
        print(40*"~~~~","\n\n")
        print("All Buyers\n")
        print(40*"~~~~","\n")
        try:
            file=open("prodlist.dat","rb")
            prod=pickle.load(file)
            for x in prod:
                if x[6] != []:
                    for i in x[6]:
                        print("%-3s"%x[0],"%-5s"%x[1],"%-10s"%i[0],"%-10s"%x[2],"%-10s"%x[3],"%-3s"%i[1],"%-20s"%i[4],"%-7s"%x[5],"%-7s"%i[3],"%-40s"%i[2])
                        #print("%-3s"%l.sno,"%-5s"%l.prodno,"%-10s"%l.buyer,"%-10s"%l.prodname,"%-10s"%l.prodtype,"%-3s"%l.buyqnt,"%-20s"%l.date,"%-7s"%l.price,"%-7s"%l.tprice,"%-40s"%l.address)
            file.close()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")
        

    while True:

        print(40*"~~~~","\n\n")
        print("                             Grossary Management\n")
        print(40*"~~~~","\n")
        print("""
1.  Add Product
2.  Display All Products
3.  Display Buyers
4.  Search Products
5.  Search Product By Catagory Type
6.  Display Catagory Type
7.  Modify Product Details
8.  Remove Product
9.  Remove All Products
10. Exit
    """)
        try:
            ch=int(input("Type Your Choice : "))
            if(ch==1):
                new_prod()
            elif(ch==2):
                disp_all()
            elif(ch==3):
                disp_buyer()
            elif(ch==4):
                disp_prod()
            elif(ch==5):
                disp_type()
            elif(ch==6):
                display_type()
            elif(ch==7):
                modify_prod()
            elif(ch==8):
                remove_prod()
            elif(ch==9):
                remove()
            elif(ch==10):
                break
            else:
                print("INVALID CHOICE")
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        

#Modify Product
def modify_prod():
    try:
        z=0
        n=int(input("Type Serial No. Or Product No. : "))
        file=open("prodlist.dat","rb")
        prod = pickle.load(file)
        file.close()
        for x in prod:
            if(x[0] == n or x[1] == n):
                z = 1
        if z == 0:
            print("Product not found, enter a valid number")
        else:
            for x in prod:
                if x[0] == n or x[1] == n:
                    print("Product Found:")
                    print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
                    print("%-4s"%x[0],"%-7s"%x[1],"%-35s"%x[2],"%-12s"%x[3],"%-8s"%x[4],"%-5s"%x[5])
                    print("Enter New Data")
                    x[2] = input("Type Product Name : ")
                    x[3] = input("Type Product Type : ")
                    x[4] = int(input("Type Product Quantity : "))
                    x[5] = int(input("Type Product Price : "))
        file = open("prodlist.dat", "wb")
        pickle.dump(prod, file)
        print("Product Modified Successfuly")
        file.close()
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")
    except EOFError:
        file.close()
    except IOError:
        print("File Not Found")
    input("Press Enter To Continue...")

#Display Product By Type
def disp_type():
    print(40*"~~~~","\n\n")
    print("              Search By Product Catagory Type\n")
    print(40*"~~~~","\n")
    try:
        z=0
        pl=input("Type Product Type : ")
        file=open("prodlist.dat","rb")
        prod = pickle.load(file)
        file.close()
        for x in prod:
            if(x[3]==pl):
                z=1
        if z==1:
            print("Product Found:")
            print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
            for x in prod:
                if x[3] == pl:
                    print("%-4s"%x[0],"%-7s"%x[1],"%-35s"%x[2],"%-12s"%x[3],"%-8s"%x[4],"%-5s"%x[5])       
        else:
            print("Product Not Found")
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

#Display Product Type
def display_type():
    print(40*"~~~~","\n\n")
    print("              Product Catagory Type\n")
    print(40*"~~~~","\n")
    try:
        z=0
        file=open("prodlist.dat","rb")
        prod = pickle.load(file)
        file.close()
        a = list(set([i[3] for i in prod]))
        for i in a:
            print(i)
    except ValueError:
        print("Please Type Integer Number")
        input("Press Enter To Continue...")        
    except EOFError:
        file.close()
        if(z==0):
            print("Product Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

def buyer():
    def prod_buy():

        print(40*"~~~~","\n\n")
        print("                                    Buy Product\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=int(input("Type Product Serial No. or Product No. : "))
            #reading the data from the db:
            file=open("prodlist.dat","rb")
            prod=pickle.load(file)
            file.close()
            i = 0
            for x in prod:
                if x[0]==pl or x[1]==pl:
                    z=1
                    break
                else:
                    i+=1
            if z==1:
            #product found
                print("Product:")
                print("%-3s"%"Sno.","%-5s"%"ProdNo.","%-35s"%"Name","%-12s"%"Type","%-3s"%"Quantity","%-7s"%"Price")
            #Displaying prod:
                print("%-4s"%prod[i][0],"%-7s"%prod[i][1],"%-35s"%prod[i][2],"%-12s"%prod[i][3],"%-8s"%prod[i][4],"%-5s"%prod[i][5])
            #making the customer buy:
                #prod[i] is the prod to be bought
                #chcking if product is available
                if(prod[i][4]==0):
                    print("Sorry this product is Currently Product Not Available")
                else:
                #asking the customer details:
                    buyer = []
                    buyer.append(input("Type Customer name:"))
                    qnt=int(input("How Much Quantity You Want To Buy : "))
                    if(qnt<=prod[i][4]):
                        prod[i][4]-=qnt
                        buyer.append(qnt)
                    else:
                        print("Sorry, You Cannot Buy More Than ",prod[i][4]," Units Of Quantity")
                        buyer.append(prod[i][4])                        
                        prod[i][4] = 0
                    buyer.append(input("Type Customer Address : "))
                    buyer.append((buyer[1])*(prod[i][5]))
                    buyer.append(t.ctime())
                    print("Your Total Price is : ", buyer[3])
                    print("Date/Time : ",buyer[4])
                    prod[i][6].append(buyer)
                #saving the current details back to database
            else:
                print("Product Not Found")
            file = open("prodlist.dat", "wb")
            pickle.dump(prod, file)
            file.close()
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except IOError:
            print("File Not Found")

#search Product
    def prod_disp():

        print(40*"~~~~","\n\n")
        print("                                 Search Orders By Searial No. or Product No.\n")
        print(40*"~~~~","\n")
        try:
            z=0
            pl=int(input("Type Product Serial No. or Product No. : "))
            file=open("prodlist.dat","rb")
            prod=pickle.load(file)
            file.close()
            i = 0
            for x in prod:
                if x[0]==pl or x[1]==pl:
                    z=1
                    break
                else:
                    i+=1
            if z==1:
                j = 1
                print("Product found")
                if prod[i][6] == []:
                    print("But, this hasn't been bought yet")
                else:
                    print("Serial No. : ", prod[i][0])
                    print("Product No. : ", prod[i][1])
                    print("Product Name. : ", prod[i][2])
                    print("Product Type : ", prod[i][3])
                    print("Product Quantity: ", prod[i][4])
                    for x in prod[i][6]:
                        print(4*"---")
                        print("Customer ",j,":")
                        print("Customer Name : ",x[0])     
                        print("Quantity Bought: ",x[1])
                        print("Day/Date/Time : ",x[4])
                        print("Total Price : ",x[3])
                        print("Customer Address : ",x[2])                    
                        j+=1
            else:
                print("Product not found")     
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        
        except EOFError:
            file.close()
            if(z==0):
                print("No Orders Available")
            print(40*"~~~~")
            input("Press Enter To Continue...")
        except IOError:
            print("File Not Found")

    while True:

        print(40*"~~~~","\n\n")
        print("                                  Stock Management System\n")
        print("                                  Dev. By Saksham\n")
        print(40*"~~~~","\n")
        print("""
1. Buy Product
2. Display All Products
3. Orders
4. Search Products
5. Search Product By Type
6. Display Product Type
7. Exit
    """)
        try:
            ch=int(input("Type Your Choice : "))
            if(ch==1):
                prod_buy()
            elif(ch==2):
                disp_all()
            elif(ch==4):
                disp_prod()
            elif(ch==3):
                prod_disp()
            elif(ch==5):
                disp_type()
            elif(ch==6):
                display_type()
            elif(ch==7):
                print(40*"~~~~")
                print("                           Thank You For Using My Program         ")
                print(40*"~~~~")
                break
            else:
                print("INVALID CHOICE")
        except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")        

while True:
    os.system("title Program Made By Saksham")
    print(40*"~~~~","\n\n")
    print("                             Please Choose Your Catagory\n")
    print(40*"~~~~","\n")
    print("""
1. Seller
2. Buyer
3. Exit""")
    try:
        ch=int(input("Type Your Choice : "))
        if(ch==1):
            cc=input("Type Seller Password : ")
            if(cc=="Saksham"):
                seller()
            else:
                print("You are Not Allowed To Seller's Area")
                input("Press Enter To Continue...")
                buyer()
        elif(ch==2):
            buyer()
        elif(ch==3):
            print(40*"~~~~")
            print("                                   Thank You For Using My Program         ")
            print(40*"~~~~")
            break
        else:
            print("INVALID CHOICE")
    except ValueError:
            print("Please Type Integer Number")
            input("Press Enter To Continue...")