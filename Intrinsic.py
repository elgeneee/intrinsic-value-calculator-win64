from tkinter import *
from tkinter import ttk
from tkinter import font
import backend

root = Tk()

root.title("Intrinsic Value Calculator")
root.geometry("680x540") #wxh
root.resizable(width=False, height = False)
root.iconbitmap("intrinsic_icon.ico")

def calc():
    cash_flow_projected = [0,0,0,0,0,0,0,0,0,0]
    discount_factor = [0,0,0,0,0,0,0,0,0,0]
    discount_value = [0,0,0,0,0,0,0,0,0,0]
    discount_rate = 0
    try:
        if operating_cash_flow.get()!=0 and beta.get()!=0 and total_debt.get()!=0 and cash_and_short_term_investment.get() !=0 and growth_rate_y1y5.get() != 0 and growth_rate_y6y10.get()!=0 and no_of_shares_outstanding.get()!=0 and ticker.get()!='':
            error_message.config(text="")
            cash_flow_projected[0] = operating_cash_flow.get() * (1+(growth_rate_y1y5.get()/100))
            cash_flow_projected[1] = cash_flow_projected[0] * (1+(growth_rate_y1y5.get()/100))
            cash_flow_projected[2] = cash_flow_projected[1] * (1+(growth_rate_y1y5.get()/100))
            cash_flow_projected[3] = cash_flow_projected[2] * (1+(growth_rate_y1y5.get()/100))
            cash_flow_projected[4] = cash_flow_projected[3] * (1+(growth_rate_y1y5.get()/100))
            cash_flow_projected[5] = cash_flow_projected[4] * (1+(growth_rate_y6y10.get()/100))
            cash_flow_projected[6] = cash_flow_projected[5] * (1+(growth_rate_y6y10.get()/100))
            cash_flow_projected[7] = cash_flow_projected[6] * (1+(growth_rate_y6y10.get()/100))
            cash_flow_projected[8] = cash_flow_projected[7] * (1+(growth_rate_y6y10.get()/100))
            cash_flow_projected[9] = cash_flow_projected[8] * (1+(growth_rate_y6y10.get()/100))

            if beta.get() < 0.80:
                discount_rate = 0.05
            elif 0.80 <= beta.get() < 1.05:
                discount_rate = 0.06
            elif 1.05 <= beta.get() < 1.15:
                discount_rate = 0.068
            elif 1.15 <=beta.get() < 1.25:
                discount_rate = 0.07
            elif 1.25 <= beta.get() < 1.35:
                discount_rate = 0.079
            elif 1.35 <= beta.get() < 1.45:
                discount_rate = 0.08
            elif 1.45 <= beta.get() <= 1.60:
                discount_rate = 0.089
            else: 
                discount_rate = 0.09

            total = 0
            for i in range(10):
                discount_factor[i] = 1/((discount_rate+1)**(i+1))
                discount_value[i] = discount_factor[i] * cash_flow_projected[i]
                total += discount_value[i]

            intrinsic_value = total/no_of_shares_outstanding.get()
            dps = total_debt.get()/no_of_shares_outstanding.get()
            cps = cash_and_short_term_investment.get()/no_of_shares_outstanding.get()

            intrinsic_value = intrinsic_value - dps + cps
            intrinsic_value_formatted = "{:.2f}".format(intrinsic_value)
            pv.configure(text = "{:.2f}".format(total))
            cash_per_share.configure(text = "{:.2f}".format(cps))
            debt_per_share.configure(text = "{:.2f}".format(dps))
            intrinsic_value_per_share.configure(text = "{:.2f}".format(intrinsic_value))

            list2 = [ticker.get().upper(), intrinsic_value_formatted]
            return(list2)
            
        else:
            error_message.config(text="Error: Please ensure all fields are filled")
    except TclError:
        error_message.config(text="Error: Insert numbers only")        
    
def clear():    
    ticker_ENTRY.delete(0,END)
    operating_cash_flow_ENTRY.delete(0,END)
    beta_ENTRY.delete(0,END)
    total_debt_ENTRY.delete(0,END)
    cash_and_short_term_investment_ENTRY.delete(0,END)
    growth_rate_y1y5_ENTRY.delete(0,END)
    growth_rate_y6y10_ENTRY.delete(0,END)
    no_of_shares_outstanding_ENTRY.delete(0,END)
    

    operating_cash_flow_ENTRY.insert(0,0)
    beta_ENTRY.insert(0,0)
    total_debt_ENTRY.insert(0,0)
    cash_and_short_term_investment_ENTRY.insert(0,0)
    growth_rate_y1y5_ENTRY.insert(0,0)
    growth_rate_y6y10_ENTRY.insert(0,0)
    no_of_shares_outstanding_ENTRY.insert(0,0)

def view_all():
    list1.delete(0,END)
    for row in backend.view():
        entry = "  "
        entry += str(row[0])
        for i in range(5-len(str(row[0]))):
            entry += " "
        entry += "    " + row[1]
        for i in range(10-len(row[1])):
            entry += " "
        entry += "        " + row[2]
        for i in range(10-len(row[2])):
            entry += " "
        entry += "   " + row[3]
        list1.config(font = 'TkFixedFont')

        list1.insert(END, entry)

def add_entry():
    backend.insert(calc()[0], calc()[1])
    view_all()

def get_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_str = list1.get(index)
    selected_list = selected_str.split()
    selected_list[0] = int(selected_list[0])
    selected_tuple = tuple(selected_list)
    
def delete_entry():
    backend.delete(selected_tuple[0])
    view_all()
     
##data_entry##
ticker_LABEL = Label(root, text = 'Ticker: ')
ticker_LABEL.place(x=0,y=10)
ticker = StringVar()
ticker_ENTRY = Entry(root, textvariable = ticker)
ticker_ENTRY.place(x=145, y=8, width = 60)

operating_cash_flow_LABEL = Label(root, text = 'Operating Cash Flow: ')
operating_cash_flow_LABEL.place(x=0, y=50)
operating_cash_flow = DoubleVar()
operating_cash_flow_ENTRY = Entry(root, textvariable = operating_cash_flow)
operating_cash_flow_ENTRY.place(x=145, y=48, width = 100)

beta_LABEL = Label(root, text = 'Beta: ')
beta_LABEL.place(x=0 , y= 90)
beta = DoubleVar()
beta_ENTRY = Entry(root, textvariable = beta)
beta_ENTRY.place(x=145 , y= 88, width = 50)

total_debt_LABEL = Label(root, text = 'Total Debt(LT + ST): ')
total_debt_LABEL.place(x = 0, y = 130)
total_debt = DoubleVar()
total_debt_ENTRY = Entry(root, textvariable = total_debt)
total_debt_ENTRY.place(x=145 , y= 128, width = 100)

cash_and_short_term_investment_LABEL = Label(root, text = 'Cash & Short Term Investment:  ')
cash_and_short_term_investment_LABEL.place(x = 320, y = 10)
cash_and_short_term_investment = DoubleVar()
cash_and_short_term_investment_ENTRY = Entry(root, textvariable = cash_and_short_term_investment)
cash_and_short_term_investment_ENTRY.place(x=525 , y= 8, width = 100)

growth_rate_y1y5_LABEL = Label(root, text = 'Growth Rate (Yr1-Yr5): ')
growth_rate_y1y5_LABEL.place(x = 320, y = 50)
growth_rate_y1y5 = DoubleVar()
growth_rate_y1y5_ENTRY = Entry(root, textvariable = growth_rate_y1y5)
growth_rate_y1y5_ENTRY.place(x=525 , y= 48, width = 50)

percentage_LABEL = Label(root, text = '%')
percentage_LABEL.place(x=580, y =50)
percentage_LABEL2 = Label(root, text = '%')
percentage_LABEL2.place(x=580, y =90)

growth_rate_y6y10_LABEL = Label(root, text = 'Growth Rate (Yr6-Yr10): ')
growth_rate_y6y10_LABEL.place(x = 320, y = 90)
growth_rate_y6y10 = DoubleVar()
growth_rate_y6y10_ENTRY = Entry(root, textvariable = growth_rate_y6y10)
growth_rate_y6y10_ENTRY.place(x=525 , y= 88, width = 50)

no_of_shares_outstanding_LABEL = Label(root, text = 'No. of Shares Outstanding: ')
no_of_shares_outstanding_LABEL.place(x=320 , y= 130)
no_of_shares_outstanding = DoubleVar()
no_of_shares_outstanding_ENTRY = Entry(root, textvariable = no_of_shares_outstanding)
no_of_shares_outstanding_ENTRY.place(x=525 , y= 128, width = 100)

million_LABEL = Label(root, text = 'millions')
million_LABEL.place(x=250, y=50)
million_LABEL1 = Label(root, text = 'millions')
million_LABEL1.place(x=250, y=128)
million_LABEL2 = Label(root, text = 'millions')
million_LABEL2.place(x=630, y=128)
million_LABEL3 = Label(root, text = 'millions')
million_LABEL3.place(x=630, y=0)

##results##
pv_LABEL = Label(root, text = 'PV of 5yr Cash Flow: ')
pv_LABEL.place(x=250, y=190)
pv = Label(root, text = '-')
pv.place(x=400, y = 190)

cash_per_share_LABEL = Label(root, text = '(+)Cash per Share: ')
cash_per_share_LABEL.place(x=250, y=220)
cash_per_share = Label(root, text = '-')
cash_per_share.place(x=400, y=220)

debt_per_share_LABEL= Label(root, text = '(-)Debt per Share: ', anchor = 'w')
debt_per_share_LABEL.place(x=255, y=250)
debt_per_share = Label(root, text = '-')
debt_per_share.place(x=400, y=250)

intrinsic_value_per_share_LABEL = Label(root, text = 'Intrinsic Value: ', anchor = 'w')
intrinsic_value_per_share_LABEL.place(x=255, y=280)
intrinsic_value_per_share = Label(root, text = '-', font = ('calibre',20,'bold'))
intrinsic_value_per_share.place(x=400, y=270)

error_message = Label(root, text = '', fg= 'red')
error_message.place(x = 460, y = 290)


##listbox & Scrollbar
my_frame = Frame(root)
sb1 = Scrollbar(my_frame, orient = VERTICAL)
list1 = Listbox(my_frame, width = 52, height = 14 , yscrollcommand = sb1)
sb1.config(command = list1.yview)
sb1.pack(side = RIGHT, fill = Y)
my_frame.pack(side = LEFT , padx = 10, pady = (310,0))
list1.pack()
list1.bind('<<ListboxSelect>>', get_row)

##button##
calc_button = Button(root, text = 'Calculate',command = calc, width = 25, height = 2)
calc_button.place(x = 460, y = 310)

add_button = Button(root, text = 'Add Entry',command = add_entry, width = 25, height = 2)
add_button.place(x = 460, y = 355)

delete_button = Button(root,text = 'Delete Entry', command = delete_entry, width = 25, height = 2)
delete_button.place(x = 460, y = 400)

view_all_button = Button(root, text = 'View All',command = view_all, width = 25, height = 2)
view_all_button.place(x = 460, y = 445)

clear_button = Button(root, text = 'Clear', command = clear, width = 25, height = 2)
clear_button.place(x = 460, y = 490)

view_all()
clear()
root.mainloop()

