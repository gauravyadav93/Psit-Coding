def Ticket_Booking(No_of_Tickets):
    if(No_of_Tickets <= 2):
        Total_price = cost_of_ticket*No_of_Tickets
        print(Total_price)
    elif(No_of_Tickets >= 2 and No_of_Tickets<6):
        Actual_price = cost_of_ticket*No_of_Tickets
        Discounted_price = 2000 -((5*cost_of_ticket)/100 + (7*cost_of_ticket)/100 + (9*cost_of_ticket)/100 + (11*cost_of_ticket)/100 )
        print("Actual_price:",Actual_price)
        print("Discounted_price:"Discounted_price)
    else:
        print("Your NUmber OF ticket is not valid")
            
            

No_of_Tickets = int(input("enter number of tickets:"))
cost_of_ticket = 500
res = Ticket_Booking(No_of_Tickets)
print(res)
