from tkinter import *
import sqlite3

# Global Area
# ============================================================================
# Creating a tk object to create the main window with adjusting features
root = Tk()

root.title('Car Rental Database')
root.geometry("400x400")


# Connecting to sqlite3

connection = sqlite3.connect('CarRental2019.db')

# =============================================================================



# Requirement 1 --------------------------------
# This function prompts the user to register as a new customer in the Car Rental database
# This function takes no parameters
def custInfo():

    # Creating text fields with labels for the user to enter
    # information as a new customer
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    name = Entry(newWindow, width=30)
    name.grid(row=0, column=1, padx=20, pady=10)

    phone = Entry(newWindow, width=30)
    phone.grid(row=1, column=1, pady=10)

    # Creating the labels corresponding to each entry

    lname = Label(newWindow, text='Name')
    lname.grid(row=0, column=0, pady=10)

    lphone = Label(newWindow, text='Phone')
    lphone.grid(row=1, column=0, pady=10)

    submit_btn = Button(newWindow, text='Add Customer',
                        command=lambda: addCustomerDB(name, phone, newWindow))
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    save_changes_btn = Button(
        newWindow, text="Exit Window", command=newWindow.destroy)
    save_changes_btn.grid(row=8, column=0, columnspan=2,
                          pady=10, padx=10, ipadx=140)




# Requirement 1 --------------------------------
# This function Inserts a new vehicle to the CarRental2019 database
# This function takes: -
# Customer Name
# Customer Phone Number
# The Tkinter Parent Window
def addCustomerDB(name, phone, newWindow):

    # Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO CUSTOMER VALUES (:CustID ,:Name, :Phone)",
		{
            'CustID': None,
			'Name': name.get(),
			'Phone': phone.get()
		})

	# commit changes
    submit_conn.commit()

	# close the DB connection
    submit_conn.close()

    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    temp.title('Update')

    ltemp = Label(temp, text='Customer Added -- Rows Modified (1)\n' + name.get() + ' ' + phone.get() + ' ' +'\n')
    ltemp.grid(row=0, column=1, padx=20, pady=10)

    exbutton = Button(temp, text="Ok", command=temp.destroy)
    exbutton.grid(row=1, column=1, padx=20, pady=10)




# Requirement 2 --------------------------------
# This function prompts the user to insert a new vehicle into the CarRental2019 database
# This function takes no parameters
def VecInfo():
    # Creating text fields with labels for the user to enter
    # information as a new vehicle
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    vin = Entry(newWindow, width=30)
    vin.grid(row=0, column=1, padx=20, pady=10)

    description = Entry(newWindow, width=30)
    description.grid(row=1, column=1, pady=10)

    year = Entry(newWindow, width=30)
    year.grid(row=2, column=1, pady=10)

    type = Entry(newWindow, width=30)
    type.grid(row=3, column=1, pady=10)

    category = Entry(newWindow, width=30)
    category.grid(row=4, column=1, pady=10)

    # Creating the labels corresponding to each entry

    lvin = Label(newWindow, text='VIN')
    lvin.grid(row=0, column=0, pady=10)

    ldescription = Label(newWindow, text='Description')
    ldescription.grid(row=1, column=0, pady=10)

    lyear = Label(newWindow, text='Year')
    lyear.grid(row=2, column=0, pady=10)

    ltype = Label(newWindow, text='Type')
    ltype.grid(row=3, column=0, pady=10)

    lcategory = Label(newWindow, text='Category')
    lcategory.grid(row=4, column=0, pady=10)

    submit_btn = Button(newWindow, text='Add Vehicle ', command=lambda: addVehicleDB(
        vin, description, year, type, category, newWindow))
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=140)

    save_changes_btn = Button(
        newWindow, text="Exit Window", command=newWindow.destroy)
    save_changes_btn.grid(row=8, column=0, columnspan=2,
                          pady=10, padx=10, ipadx=140)




# Requirement 2 --------------------------------
# This function Inserts a new vehicle to the CarRental2019 database
# This function takes: -
# VehicleID
# Description
# Year
# Type
# Category
# The Tkinter Parent Window
def addVehicleDB(vin, description, year, type, category, newWindow):

    # Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()
    
    # Inserting a new vehicle to the CarRental2019 database
    submit_cur.execute("INSERT INTO VEHICLE VALUES (:VehicleID, :Description, :year, :type, :category)",
		{
			'VehicleID': vin.get(),
			'Description': description.get(),
			'year': year.get(),
			'type': type.get(),
			'category': category.get()
		})
   	# commit changes  
    submit_conn.commit()

	# close the DB connection    
    submit_conn.close()

    # Interactivity Monitor with users
    temp =Toplevel(newWindow)
    temp.title('Update')


    ltemp = Label(temp, text='Vehicle Added -- Rows Modified (1)\n' + vin.get() + ' ' + description.get() + ' ' + year.get() + ' ' + type.get() + ' '+ category.get() + ' ' +'\n')
    ltemp.grid(row=0, column=1, padx=20, pady=10)

    exbutton = Button(temp,text = "Ok",command = temp.destroy)
    exbutton.grid(row = 1, column = 1, padx = 20,pady=10)



# Requirement 3 --------------------------------
# This function prompts the user to book an available rental with an option to view the cars available in the database
# This function takes no parameters
def RentInfo():
    # Creating text fields with labels for the user to enter
    # information for an available rental
    newWindow = Toplevel(root)
    newWindow.geometry('450x650')

    custId = Entry(newWindow, width = 30)
    custId.grid(row = 0, column = 1, padx = 20,pady=10)

    vID = Entry(newWindow, width = 30)
    vID.grid(row = 1, column = 1, padx = 20,pady=10)

    category = Entry(newWindow, width = 30)
    category.grid(row = 2, column = 1,pady=10)

    type = Entry(newWindow, width = 30)
    type.grid(row = 3, column = 1,pady=10)

    startDate = Entry(newWindow, width = 30)
    startDate.grid(row = 4, column = 1,pady=10)

    returnDate = Entry(newWindow, width = 30)
    returnDate.grid(row = 5, column = 1,pady=10)

    orderDate = Entry(newWindow, width = 30)
    orderDate.grid(row = 6, column = 1,pady=10)
    
    rentalType = Entry(newWindow, width = 30)
    rentalType.grid(row = 7, column = 1,pady=10)

    Qty = Entry(newWindow, width = 30)
    Qty.grid(row = 8, column = 1,pady=10)

    totalAmount = Entry(newWindow, width = 30)
    totalAmount.grid(row = 9, column = 1,pady=10)

    paymentDate = Entry(newWindow, width = 30)
    paymentDate.grid(row = 10, column = 1,pady=10)

    returned = Entry(newWindow, width = 30)
    returned.grid(row = 11, column = 1,pady=10)


    # Creating the labels corresponding to each entry

    lcustID = Label(newWindow, text = 'Customer ID')
    lcustID.grid(row =0, column = 0,pady=10)

    lvID = Label(newWindow, text = 'Vehicle ID')
    lvID.grid(row =1, column = 0,pady=10)

    lcategory = Label(newWindow, text = 'Car Category')
    lcategory.grid(row =2, column = 0,pady=10)

    ltype = Label(newWindow, text = 'Car Type')
    ltype.grid(row =3, column = 0,pady=10)

    lstartDate = Label(newWindow, text = 'Start Date')
    lstartDate.grid(row =4, column = 0,pady=10)

    lreturnDate = Label(newWindow, text = 'Return Date')
    lreturnDate.grid(row =5, column = 0,pady=10)

    lorderDate = Label(newWindow, text = 'Order Date')
    lorderDate.grid(row =6, column = 0,pady=10)

    lrentalType = Label(newWindow, text = 'Rental Type')
    lrentalType.grid(row =7, column = 0,pady=10)

    lQty = Label(newWindow, text = 'Qty')
    lQty.grid(row =8, column = 0,pady=10)

    ltotalAmount = Label(newWindow, text = 'Total Amount')
    ltotalAmount.grid(row =9, column = 0,pady=10)

    lpaymentDate = Label(newWindow, text = 'Payment Date')
    lpaymentDate.grid(row =10, column = 0,pady=10)

    lreturned = Label(newWindow, text = 'Return Status')
    lreturned.grid(row =11, column = 0,pady=10)


    # An option for the user to view the cars available to rent
    submit_btn = Button(newWindow, text ='Show Cars available', command = lambda: carsAvailable(newWindow))
    submit_btn.grid(row = 12, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

    # An option for the user to insert a rental
    submit_btn2 = Button(newWindow, text ='Add Rental', command = lambda: insertRental(custId,vID,startDate,returnDate,orderDate,rentalType,Qty,totalAmount, paymentDate,returned, newWindow))

    submit_btn2.grid(row = 13, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)




# Requirement 3 --------------------------------
# This function retrieves the cars available to rent in the CarRental2019 database 
# This function takes: -
# The Tkinter Parent Window
def carsAvailable(newWindow):

    # Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()

    # Retrieving the cars available to rent
    submit_cur.execute("SELECT V.Description FROM VEHICLE AS V, RENTAL AS R WHERE R.VehicleID = V.VehicleID AND R.Returned = 1 GROUP BY V.Description", ())

    # Fetching the data improted from the cursor
    output_records = submit_cur.fetchall()

    print_record = ''

    # Formatting the records
    rowCount = 0
    for output_record in output_records:
        print_record += str(str(output_record[0])+ " " + "\n")
        rowCount += 1
    

    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    temp.title('Available Cars')

    iq_label = Label(temp, text = "Available Cars -- Rows Modified ("+ str(rowCount) +"):-\n"+print_record)
    
    iq_label.grid(row = 0, column = 0, columnspan = 2)
	

    submit_btn2 = Button(temp, text ='Exit', command = temp.destroy)
    submit_btn2.grid(row = 1, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)




# Requirement 3 --------------------------------
# This function Inserts Information for the rental in the CarRental2019 database and shows the user that information has been updated and does not return anything
# This function takes: -
# Customer ID
# VehicleID
# Return Date
# Rental Type
# Qty
# Total Amount
# Returned Status
# The Tkinter Parent Window
def insertRental(custId,vID,startDate,returnDate,orderDate,rentalType,Qty,totalAmount, paymentDate,returned, newWindow):
    
    # Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()

    # Inserting a Rental into the database
    submit_cur.execute("INSERT INTO RENTAL VALUES (:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :Totalamount, :PaymentDate, :Returned)",
		{
			'CustID': custId.get(),
			'VehicleID': vID.get(),
			'StartDate': startDate.get(),
			'OrderDate': orderDate.get(),
			'RentalType': rentalType.get(),
            'Qty': Qty.get(),
            'ReturnDate': returnDate.get(),
            'Totalamount': totalAmount.get(),
            'PaymentDate': paymentDate.get(),
            'Returned': returned.get(),
		})
    
   	# commit changes  
    submit_conn.commit()

	# close the DB connection    
    submit_conn.close()

    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    temp.title('Update')


    ltemp= Label(temp, text ='Rental Added -- Rows Modified(1)\n'+custId.get() +" "+ vID.get() + " " + startDate.get()+ " " +orderDate.get() + " " + rentalType.get() + " " +Qty.get() + " "+ returnDate.get() + " " + totalAmount.get()+ " " + paymentDate.get() + " "+ returned.get())
    ltemp.grid(row = 0, column = 1, padx = 20,pady=10)

    exbutton = Button(temp,text = "Ok",command = temp.destroy)
    exbutton.grid(row = 1, column = 1, padx = 20,pady=10)





# Requirement 4 --------------------------------
# This function handles the return of the a vehicle by prompting the user to enter his/her information to pay for the vehicle and an option to pay or exit
# This function has no parameters
def handleReturnedRental():

    # Creating text fields with labels for the user to enter
    # information to obtain the vehicle payment status
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    custName = Entry(newWindow, width = 30)
    custName.grid(row = 0, column = 1, padx = 20,pady=10)

    custID = Entry(newWindow, width = 30)
    custID.grid(row = 1, column = 1,pady=10)

    vID = Entry(newWindow, width = 30)
    vID.grid(row = 2, column = 1,pady=10)

    returnDate = Entry(newWindow, width = 30)
    returnDate.grid(row = 3, column = 1,pady=10)

    # Creating the labels corresponding to each entry

    lcustName = Label(newWindow, text = 'Customer Name')
    lcustName.grid(row =0, column = 0,pady=10)

    lcustID = Label(newWindow, text = 'Customer ID')
    lcustID.grid(row =1, column = 0,pady=10)

    lvID = Label(newWindow, text = 'VehicleID')
    lvID.grid(row =2, column = 0,pady=10)

    lreturnDate = Label(newWindow, text = 'Return Date')
    lreturnDate.grid(row =3, column = 0,pady=10)


    submit_btn = Button(newWindow, text ='Payment Due', command = lambda: paymentDue(custName,custID,vID,returnDate, newWindow))
    submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


# Requirement 4 --------------------------------
# This function retrieves the user information from the CarRental2019 database and prompt the user to pay his/her bill with offering an option to pay or exit
# After a payment is made, the user will have the new updated balance
# This function takes: -
# Customer Name
# Customer ID
# Vehicle ID
# The Tkinter Parent Window
def paymentDue(custName,custID,vID,returnDate, newWindow):


    #Connecting again to make the access cocurrent active
    iq_conn = sqlite3.connect('CarRental2019.db')
    
    # Creating a cursor to execute queries and commit changes
    iq_cur = iq_conn.cursor()

    # Retrieving the TotalAmount of the vehicles 
    iq_cur.execute("SELECT R.TotalAmount FROM RENTAL AS R JOIN CUSTOMER AS C ON R.CustID = C.CustID WHERE R.ReturnDate = ? AND C.Name = ? AND R.VehicleID = ?", (returnDate.get(), custName.get(),vID.get()))

    # Fetching the data improted from the cursor
    output_records = iq_cur.fetchall()

    print_record = ''
    
    # Formatting the records
    for output_record in output_records:
        print_record += (str(str(output_record[0])) + " " + "\n")
    

    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    
    temp.title("Payment")

    iq_label = Label(temp, text = "The payment amount due is\n "+print_record)
    
    iq_label.grid(row = 0, column = 0, columnspan = 2)
	

    # This button handles the payment
    submit_btn = Button(temp, text ='Pay', command = lambda: updatePaymentDay(custID,vID))
    submit_btn.grid(row = 1, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

    # An option to exit the window
    submit_btn2 = Button(temp, text ='Exit', command = temp.destroy)
    submit_btn2.grid(row = 2, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

	#commit changes
    iq_conn.commit()

	#close the DB connection
    iq_conn.close()


# Requirement 4 --------------------------------
# This function makes issues the payment for the user and updates the database with the new balance
# This function takes: -
# Customer Name
# Vehicle ID
def updatePaymentDay(custID,vID):
    #Connecting again to make the access cocurrent active
    submit_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    submit_cur = submit_conn.cursor()
    
    # Updating the user's balance when the transaction is successful
    submit_cur.execute("UPDATE RENTAL SET Returned = 1, PaymentDate = '2022-05-08',totalAmount = 0 WHERE CustID = :CustID AND VehicleID = :VehicleID",
		{
			'CustID': custID.get(),
            'VehicleID': vID.get()	
            
		})

	#commit changes
    submit_conn.commit()

	# close the DB connection    
    submit_conn.close()


# Requirement 5A --------------------------------
# This function prompts the user to enter information about a customer to retrieve by a customer ID or a customer name or neither
# This function takes no parameters
def lookCust():
    # Creating text fields with labels for the user to enter
    # information to obtain information about the customer
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    custName = Entry(newWindow, width = 30)
    custName.grid(row = 0, column = 1, padx = 20,pady=10)

    custID = Entry(newWindow, width = 30)
    custID.grid(row = 1, column = 1,pady=10)

    # Creating the labels corresponding to each entry

    lcustName = Label(newWindow, text = 'Customer Name')
    lcustName.grid(row =0, column = 0,pady=10)

    lcustID = Label(newWindow, text = 'Customer ID')
    lcustID.grid(row =1, column = 0,pady=10)


    submit_btn = Button(newWindow, text ='Look up Customer', command = lambda: displayCustomerInformation(custName,custID, newWindow))
    submit_btn.grid(row = 4, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)


# Requirement 5A --------------------------------
# This function displays the customer information for a corresponding answer based on what the customer entered
# This function takes: -
# Customer Name
# Customer ID
# The Tkinter Parent Window
def displayCustomerInformation(custName,custID, newWindow):
    
    #Connecting again to make the access cocurrent active
    iq_conn = sqlite3.connect('CarRental2019.db')
    
    # Creating a cursor to execute queries and commit changes
    iq_cur = iq_conn.cursor()

    # if the user only entered a customer name
    if (not len(custName.get()) == 0):
        iq_cur.execute("SELECT CustomerID, CustomerName, SUM(RemainingBalance) FROM vRentalInfo WHERE CustomerName LIKE ? GROUP BY CustomerName ORDER BY COUNT(RemainingBalance) DESC", ("%" + custName.get() + "%" ,))

    # if the user both customer name and id
    elif (not len(custName.get()) == 0) and  (custID.get().isdigit()) :
        iq_cur.execute("SELECT CustomerID, CustomerName, SUM(RemainingBalance) FROM vRentalInfo WHERE CustomerID LIKE ? AND CustomerName LIKE ? GROUP BY CustomerID ORDER BY COUNT(RemainingBalance) DESC", (custName.get(),custID.get(),))

    # if the user only entered a customer id
    elif (custID.get().isdigit()):
        iq_cur.execute("SELECT CustomerID, CustomerName, SUM(RemainingBalance) FROM vRentalInfo WHERE CustomerID LIKE ? GROUP BY CustomerID ORDER BY COUNT(RemainingBalance) DESC", (custID.get(),))
    
    # if the user did not enter a customer id nor a customer name
    else:
        iq_cur.execute("SELECT CustomerID, CustomerName, SUM(RemainingBalance) FROM vRentalInfo GROUP BY CustomerName ORDER BY COUNT(RemainingBalance) DESC")
   
    
    # Fetching the data improted from the cursor
    output_records = iq_cur.fetchall()


    print_record = ''
    
    # Formatting the records
    rowCount = 0
    for output_record in output_records:
        print_record += (str(str(output_record[0]))) + "  " +(str(str(output_record[1])) + "  " +(str(output_record[2])) + "  " "\n")
        rowCount += 1


    
    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    temp.title("Customer Book")


    iq_label = Label(temp, text = "--Customers--"+ "Rows Modified ("+ str(rowCount) +")--\n" +print_record)
    
    iq_label.grid(row = 0, column = 0, columnspan = 2)
	
    submit_btn2 = Button(temp, text ='Okay', command = temp.destroy)
    submit_btn2.grid(row = 2, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

	#commit changes
    iq_conn.commit()

	#close the DB connection
    iq_conn.close() 



# Requirement 5B --------------------------------
# This function prompts the user to enter information about a Vehicle to retrieve by a Vehicle Description or a VIN or niether
# This function takes no parameters
def lookVec():
    # Creating text fields with labels for the user to enter
    # information to obtain information about the Vehicle
    newWindow = Toplevel(root)
    newWindow.geometry('400x400')

    vehicle = Entry(newWindow, width = 30)
    vehicle.grid(row = 0, column = 1, padx = 20,pady=10)

    VIN = Entry(newWindow, width = 30)
    VIN.grid(row = 1, column = 1,pady=10)

    # Creating the labels corresponding to each entry
    
    lVehicle = Label(newWindow, text = 'Vehicle Name')
    lVehicle.grid(row =0, column = 0,pady=10)

    lVIN = Label(newWindow, text = 'VIN')
    lVIN.grid(row =1, column = 0,pady=10)


    submit_btn = Button(newWindow, text ='Look up Vehicle', command = lambda: displayVehicleInformation(vehicle,VIN, newWindow))
    submit_btn.grid(row = 4, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



# Requirement 5B --------------------------------
# This function displays the vehicle information for a corresponding answer based on what the customer entered
# This function takes: -
# Vehicle Name
# Vehicle ID
# The Tkinter Parent Window
def displayVehicleInformation(Vehicle,VIN, newWindow):

    #Connecting again to make the access cocurrent active
    iq_conn = sqlite3.connect('CarRental2019.db')

    # Creating a cursor to execute queries and commit changes
    iq_cur = iq_conn.cursor()



    # if the user only entered a vehicle description
    if (not len(Vehicle.get()) == 0):
        iq_cur.execute("SELECT VIN, Vehicle, (SUM(OrderAmount) / SUM (TotalDays)) AS DAILYPRICE FROM vRentalInfo WHERE Vehicle LIKE ? GROUP BY VIN ORDER BY (SUM(OrderAmount)/SUM(TotalDays)) ASC", ("%" + Vehicle.get() + "%" ,))

    # if the user entered both a vehicle description and a VIN
    elif (not len(Vehicle.get()) == 0) and  (not len(VIN.get())):
        iq_cur.execute("SELECT VIN, Vehicle, (SUM(OrderAmount) / SUM (TotalDays)) AS DAILYPRICE FROM vRentalInfo WHERE VIN LIKE ? AND Vehicle LIKE ? GROUP BY VIN ORDER BY (SUM(OrderAmount)/SUM(TotalDays)) ASC", (VIN.get(),Vehicle.get(),))

    # if the user only entered a VIN
    elif (not len(VIN.get()) == 0):
        iq_cur.execute("SELECT VIN, Vehicle, (SUM(OrderAmount) / SUM (TotalDays)) AS DAILYPRICE FROM vRentalInfo WHERE VIN LIKE ? GROUP BY VIN ORDER BY (SUM(OrderAmount)/SUM(TotalDays)) ASC", (VIN.get(),))
    
    # if the user did not enter a VIN nor a vehicle description
    else:
        iq_cur.execute("SELECT VIN, Vehicle, (SUM(OrderAmount) / SUM (TotalDays)) AS DAILYPRICE FROM vRentalInfo GROUP BY VIN ORDER BY (SUM(OrderAmount)/SUM(TotalDays)) ASC")
   

    # Fetching the data improted from the cursor
    output_records = iq_cur.fetchall()


    print_record = ''
    

    # Formatting the records
    rowCount = 0
    for output_record in output_records:
        print_record += (str(str(output_record[0]))) + "  " +(str(str(output_record[1])) + "  " +(str(output_record[2])) + "  " "\n")
        rowCount += 1

    # Interactivity Monitor with users
    temp = Toplevel(newWindow)
    temp.title("Vehicle Book")

    iq_label = Label(temp, text = "--Vehicles--Rows Modified ("+ str(rowCount) + ")--\n" +print_record)
    
    iq_label.grid(row = 0, column = 0, columnspan = 2)
	
    submit_btn2 = Button(temp, text ='Okay', command = temp.destroy)
    submit_btn2.grid(row = 2, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

	#commit changes
    iq_conn.commit()

	#close the DB connection
    iq_conn.close() 




# This function is the main menu entry point. It displays the options as a menu for the user to select from
# This function takes no parameters
def MainMenu():

    # Creating Widgets for the Main Menu
    welcome = Label(root,text= 'Welcome to Our Car Rental Database')
    welcome.grid(row= 1, column= 1, padx= 85,pady=5)

    opt = Label(root,text= 'Select an option from the list')
    opt.grid(row= 2, column= 1, padx= 85,pady=5)

    # First Requirement
    addCust = Button(root,text= 'Add Customer', command= custInfo)
    addCust.grid(row= 3, column= 1,pady=10)

    # Second Requirement
    addVehicle = Button(root,text= 'Add Vehicle', command= VecInfo)
    addVehicle.grid(row= 4, column= 1,pady=10)

    # Third Requirement
    addRental = Button(root,text= 'Rental Info', command= RentInfo)
    addRental.grid(row= 5, column= 1,pady=10)

    # Fourth Requirement
    returnRental = Button(root,text= 'Return and Pay', command= handleReturnedRental)
    returnRental.grid(row= 6, column= 1,pady=10)

    # Fifth Requirement
    lookByCust = Button(root,text= 'Look Up By Customer', command= lookCust)
    lookByCust.grid(row= 7, column= 1,pady=10)

    # Fifth Requirement
    lookByVehicle = Button(root,text= 'Look Up By Vehicle', command= lookVec)
    lookByVehicle.grid(row= 8, column= 1,pady=10)




    # Keeps the programming running until clicks on the exist button 
    root.mainloop()




#=== Main Starts Here ===
if __name__ == "__main__":

    MainMenu()