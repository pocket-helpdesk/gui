TICKET_PRICE = 10

tickets_remaining = 100
#Tickets left for sale
print ("There are {} tickets remaining".format(tickets_remaining))

#Get users name and assign to variable
users_name = input("What is your name? ")

#Prompt the user how many tickets would they want
ticket_quantity = input("Hey, {} how many tickets would you like to buy?  ".format(users_name))
ticket_quantity = int(ticket_quantity)

#Calculcate the price(number of tickets * price) and assig to variable
tickets_total = (TICKET_PRICE * ticket_quantity)

#output the price on screen
print("{}, your total for {} ticket('s) is S{} dolars".format(users_name, ticket_quantity, tickets_total))

#Confirm user is OK with price Y/N?
total_check = input("Is the total {} OK? Would you like to proceed? Y/N?".format(tickets_total))

#if they want to proceed
if total_check.lower() == "y":
	#print out to the screen "SOLD!"" to confim purchase
	print("Print Sold")
	#decrement the tickets remaning by the number of tickets purchsed.
	tickets_remaining -= ticket_quantity
#Otherwise...
else:
	#Thank them by name.
	print("Thank you anyways {}!".format(users_name))