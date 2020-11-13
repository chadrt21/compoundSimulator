'''
 Name: Compound Intrest Simulator
 Author: Chad Ross
 Created Date: 2018-05-14
 Last Updated: 2020-11-12
 Purpose: To educate how effective compound intrest can be
'''
import os
import datetime as dt
from pylab import *
import numpy as np
from tkinter import *
from tkinter import ttk

# Clears the screen
os.system('cls' if os.name == 'nt' else 'clear')

print("\nCompound Intrest Simulator")
print("Disclamer: This is a simulation and should not be used as a financal tool\n")

root = Tk()
root.title("Compound Intrest Simulator")

mainframe = ttk.Frame(root,padding=(12,12,50,50))

mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

amount = StringVar()
ammount_entry = ttk.Entry(mainframe,width=7,textvariable=amount)
ammount_entry.grid(column=1,row=0,sticky=E)
ttk.Label(mainframe,text="principal").grid(column=2,row=0,sticky=W)

duration = StringVar()
duration_entry = ttk.Entry(mainframe, width=7, textvariable=duration)
duration_entry.grid(column=1,row=1,sticky=E)
ttk.Label(mainframe,text="duration").grid(column=2,row=1,sticky=W)

increment = StringVar()
inc_entry = ttk.Entry(mainframe,width=7,textvariable=increment)
inc_entry.grid(column=1,row=2,sticky=E)
inc = {'Yearly deposit','Monthly deposit'}
incOption = StringVar()
incOption.set('Yearly deposit')
inc_menu = OptionMenu(mainframe,incOption, *inc)
inc_menu.grid(column=2,row=2,sticky=W)
# TODO get OptionMenu functionality to work

# TODO add output of data


def calculate(*args):
    try:
        amount1 = float(amount.get())
        duration1 = int(duration.get())
        monthlyBool = False
        repChoice = 1
        monthlyAmt = 400

        x_amount = []
        y_year = []
        intrest = []
        if duration1 <= 0:
            duration1 = 2
        percent = np.random.uniform(-0.08,0.24,duration1)
        incomePercent = np.random.uniform(0,0.12,duration1)
        yearlyAmt = monthlyAmt * 12



        # Output table
        print("Year | Duration |\t Amount |\tIntrest Amount  |\t\t Intrest")
        for index in range(0,duration1):
            intrestAmt = amount1 * percent[index]
            amount1 += intrestAmt
            intrest.append(intrestAmt)
            if monthlyBool:
                if repChoice == 1:
                    amount1 += yearlyAmt
                elif repChoice == 4:
                    yearlyAmt += yearlyAmt * incomePercent[index]
                    amount1 += yearlyAmt
                else:
                    amount1 += monthlyAmt
            x_amount.append(amount1)
            y_year.append(index+1+dt.date.today().year)
            print("%d\t%d\t%s\t%s\t%s" % (index+1+dt.date.today().year,index+1,"{0:-17,.2f}".format(amount1),
                                "{0:-17,.2f}".format(intrestAmt), "{0:-17,.2f}%".format(percent[index] * 100)))

	# 	retirementDuration = 90 - ((dt.date.today().year - 1993) + duration1)
	# 	print("Yearly amount in retirement (%d years): %s" % (retirementDuration, "{0:2,.2f}".format(amount1 / retirementDuration)))
	# 	print("Monthly amount in retirement (%d years): %s" % (retirementDuration,"{0:2,.2f}".format(amount1 / retirementDuration / 12)))

        # Display graph
        # TODO change to scatter plot
        # TODO add multiple runs per plot
        pt1 = bar(y_year, x_amount, color='black')
        pt2 = bar(y_year, intrest, color='red')
        ylabel("USD (in millions)")
        xlabel("Years")
        title("Est. Compound Intrest Projections")
        legend((pt1[0],pt2[0]),('Amount','Intrest Amount'),loc='upper left')
        ticks = np.arange(0, (max(x_amount)+1), 1000000)
        yticks(ticks, [str(x) for x in range(0,len(ticks))])
        grid(True)
        show()

        pass
    except ValueError as e:
        print("Please input correct data type")
        # TODO error check loop
    except Exception as e:
        pass

ttk.Button(mainframe,text="Calculate",command=calculate).grid(column=3,row=3,sticky=W)
root.bind('<Return>',calculate)

for child in mainframe.winfo_children():
	child.grid_configure(padx=5,pady=5)

ammount_entry.focus()
duration_entry.focus()

mainframe.columnconfigure(1,weight=1)

root.mainloop()
