# Billing-System-for-Cafe-or-Restaurant

Prerequisite- Python3 with tkinter and fpdf. 
The invoice.pdf will generate in tha same folder in which cafe.py file is located. 

Run the cafe.py file directly to open the billing window.
NOTE- Run this on python3 not python2 as there is difference in tkinter for both python versions.

You can change tax-rate on line 786 and 849 .

If you want to add any food item, follow the below mentioned steps :-
    1. Add a new variable on line 77. eg. var45=IntVar()
    2. Suppose i want to add peanuts, so add a variable on line 131. eg. varPeaNuts=StringVar()
    3. Set default value of variable added in point 1 on line 176. eg. var45.set(0)
    4. Set default value of variable added in point 2 on line 221. eg. varPeaNuts.set('0')
    5. Again do above step in line 325.
    6. Add    txtPeaNuts.configure(state=DISABLED)  on line 370.
    7. Add the below code on line 444 :
    ```ruby
          def chkPeaNuts():
                if (var45.get() == 1):
                  txtPeaNuts.configure(state=NORMAL)
                  varPeaNuts.set("")
                elif (var45.get() == 0):
                  txtPeaNuts.configure(state=DISABLED)
                  varPeaNuts.set("0")
    ```             
    8. Now add ```ruby val45=float(varPeaNuts.get())``` on line 777.
    9. In the calculation of temptotal on line 779 add on end (val45*the value of peanut within a bracket).
    10. Add these lines at the end of any block :
    ```ruby
          PeaNuts= Checkbutton(???, text='Pea Nuts\t\t( Rs. 200 )', variable=?, onvalue=1, offvalue=0, 
		   font=('arial', 12, 'bold'),  command=lambda: chkPeaNuts()).grid(row=??,column=0, sticky=W)
          txtPeaNuts = Entry(???, font=('arial', 12, 'bold'), textvariable=varPeaNuts, width=6,            
                   justify='right', state=DISABLED)
          txtPeaNuts.grid(row = ??, column = 1)
    ```    
          ??? - Add f1/f3/f2TOP/f2BOTTOM depnding on where you want to insert.
          ?? - Put (1+row value of above item),just be sure to put item at the end of any BLOCK.
	  ? - Put the variable create on first step eg.  var45.
    11. ```ruby lblspace.grid(row=?, column=0) ```,increase the value at ? by one.
    12. And there you go , now run the cafe.py file to see the changes.
    
For deleting any data follow the above procedure but instead of adding delete the fields.
GOOD LUCK !!
    
