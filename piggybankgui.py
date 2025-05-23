from tkinter import *
amount_transacted_in_chart =''

# Create main window
root = Tk()
root.title("Piggy Bank")
root.geometry("700x700")

# Label and input for account name
signinlabel=Label(text="Enter account name")
signinlabel.grid(row=1,column=2)


sign_in_input = Entry(root, width=50, borderwidth=5)
sign_in_input.grid(row=2,column=1,columnspan=3)


# Function to handle sign in and show balance
def sign_in_click():  
    if sign_in_input.get() != '':
        global account_file
        # Open or create account file
        account_file = open(  str(sign_in_input.get()) + ".txt"  , 'a+')
        account_file.seek(0)
        number = 0
        line_number = 0
        file_lines = account_file.readlines()
        # Calculate current balance
        while(line_number < len(file_lines)):    
            loop_number = number
            file_contents = file_lines[line_number].split()
            number = float(file_contents[0])
            number = number + loop_number
            line_number =  line_number + 1    
            
        show_balance = "   This is your balance: " + str(number) + "     "
        show_balance_label = Label(root, text=show_balance)
        show_balance_label.grid(row = 1, column = 4,columnspan=3)
        file_button["state"] = "normal"
        submit_button["state"] = "normal"
        input_of_amount_transacted["state"] = "normal"
        reason_input["state"] = "normal"

# Function to read and display past transactions
def read_file():
    account_file.seek(0)
    top = Toplevel()
    top.geometry("400x600")

    frame = Frame(top)
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    account_contents = account_file.readlines()
    listbox = Listbox(frame,width=50,yscrollcommand=scrollbar.set)
    listbox.insert(0,"Amount             Date                Reason")
    for item in account_contents:
        listbox.insert(END,item)
    listbox.pack(pady=15,side=LEFT)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=listbox.yview)
    frame.pack()

# Options for transaction type
options=[
    "Deposit",
    "Withdraw"
]

# Enable submit button if reason and amount are entered
def reason():
    if(input_of_amount_transacted.get() != ''):
        if(reason_input.get()!= ''):
            submit_button["state"] = "normal" 

# Dropdown for transaction type
clicked=StringVar()
clicked.set("Withdraw or Deposit")
drop = OptionMenu(root,clicked,*options,)
drop.grid(row=4,column=2)

# Entry for amount and reason, initially disabled
input_of_amount_transacted = Entry(root,width=50,state=DISABLED)
input_of_amount_transacted.grid(row=5,column=1,columnspan=3)
reason_input = Entry(root,width=50,state=DISABLED)
reason_input.grid(row=8,column=1,columnspan=3)

# Button to view past transactions
file_button = Button(root,text="See Past Transactions",command=read_file,highlightbackground='#3E4149',state="disabled")
file_button.grid(row=4,column=4)

# Function to process deposit/withdrawal and update file
def finish():
    error_label = Label(root,text="")
    if(input_of_amount_transacted.get() != ''):
        if(reason_input.get()!= ''):
            if(clicked.get()== "Deposit" or clicked.get() == "Withdraw"):
                error_label.config(text="                                                                                                                                 ")
                error_label.grid(row=10,column=2)
                global amount_transacted_in_chart
                number = 0
                line_number = 0
                account_file.seek(0)
                file_lines = account_file.readlines()
                # Calculate current balance
                while(line_number < len(file_lines)):    
                    loop_number = number
                    file_contents = file_lines[line_number].split()
                    number = float(file_contents[0])
                    number = number + loop_number
                    line_number =  line_number + 1
                amount_of_money = ''
                if(clicked.get() =="Deposit"):
                    amount_of_money = number + float(input_of_amount_transacted.get())
                    amount_transacted_in_chart = "+" + str(input_of_amount_transacted.get())
                else:        
                    if(clicked.get() == "Withdraw"):
                        amount_of_money = number - float(input_of_amount_transacted.get())
                        amount_transacted_in_chart = "-" + str(input_of_amount_transacted.get())
                show_balance = "     This is your balance: " + str(amount_of_money) + "       "
                show_balance_label = Label(root, text=show_balance)
                show_balance_label.grid(row=1, column=4,columnspan=2)

                # Get today's date for transaction
                from datetime import date
                today = date.today()
                date_for_transaction = today 

                d = 0
                b = 0

                # Format transaction line for file
                length_of_amount = len(amount_transacted_in_chart)
                length_amount_to_date = ""
                length_of_date = len(str(date_for_transaction))
                length_date_to_reason = ""
                spaces_between_titles = 15
                if(length_of_amount <= 6):
                    length_needed_more_for_less_amount = 6 - length_of_amount
                    number_of_spaces_needed_for_less_amount = length_needed_more_for_less_amount + spaces_between_titles 
                    while(d < number_of_spaces_needed_for_less_amount):
                        length_amount_to_date = length_amount_to_date + ' '
                        d = d + 1
                else:
                    length_extra_for_more_amount = length_of_amount - 6
                    number_of_spaces_needed_for_more_amount = spaces_between_titles - length_extra_for_more_amount
                    while(d < number_of_spaces_needed_for_more_amount):
                        length_amount_to_date = length_amount_to_date +  ' '
                        d = d + 1
                if(length_of_date <= 4):
                    length_needed_more_for_less_date = 4 - length_of_amount
                    number_of_spaces_needed_for_less_date = length_needed_more_for_less_date + spaces_between_titles 
                    while(b < number_of_spaces_needed_for_less_date):
                        length_date_to_reason = length_date_to_reason + ' '
                        b = b + 1
                else:
                    length_extra_for_more_date = length_of_date - 4
                    number_of_spaces_needed_for_more_date = spaces_between_titles - length_extra_for_more_date
                    while(b < number_of_spaces_needed_for_more_date):
                        length_date_to_reason = length_date_to_reason +  ' '
                        b = b + 1

                a = str(amount_transacted_in_chart) + length_amount_to_date+ str(date_for_transaction) + length_date_to_reason + str(reason_input.get()) 
                account_file.write( a + "\n")
                input_of_amount_transacted.delete(0,END)
                reason_input.delete(0,END)
            else:
                error_label.config(text="Please Choose To Deposit Or Withdraw",fg="red")
                error_label.grid(column=2,row=10)
        else:
            error_label.config(text="                       Please Enter Your reason                   ",fg="red")
            error_label.grid(row=10,column=2)
    else:
        error_label.config(text="                       Please Enter An Amount                     ",fg="red")
        error_label.grid(row=10,column=2)

# Label for reason input
show_balance = "What is the reason for the transaction"
show_balance_label = Label(root, text=show_balance)
show_balance_label.grid(row=7,column=2)


# Submit and sign in buttons
submit_button = Button(root,text="Submit",command=finish,state="disabled",highlightbackground='#3E4149')
submit_button.grid(row=9,column=2)
sign_in_button=Button(root,text="Sign in",command=sign_in_click,highlightbackground='#3E4149')
sign_in_button.grid(row = 3, column = 2)

# Handle window close event
def on_closing():
    try:
        account_file.close()
        root.destroy()
    except NameError :
        root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI event loop
root.mainloop()

