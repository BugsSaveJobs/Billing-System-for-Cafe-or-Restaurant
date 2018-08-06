# Billing-System-for-Cafe-or-Restaurant

Prerequisite- Python3 with tkinter 

Run the cafe.py file directly to open the billing window.
NOTE- Run this on python3 not python2 as there is difference in tkinter for both python versions.

You can change tax-rate on line 785 .
* The entire food menu is hard-coded in the py file.
If you want to add any food item, follow the below mentioned steps :-
    1. Add a new variable on line 76. eg. var45=IntVar()
    2. Suppose i want to add peanuts, so add a variable on line 130. eg. varPeaNuts=StringVar()
    3. Set default value of variable added in point 1 on line 175. eg. var45.set(0)
    4. Set default value of variable added in point 2 on line 220. eg. varPeaNuts.set('0')
    5. Again do above step in line 324.
    6. Add    txtPeaNuts.configure(state=DISABLED)  on line 369.
    7. Add the below code on line 443 :
    ```ruby
          def chkPeaNuts():
                if (var45.get() == 1):
                  txtPeaNuts.configure(state=NORMAL)
                  varPeaNuts.set("")
                elif (var45.get() == 0):
                  txtPeaNuts.configure(state=DISABLED)
                  varPeaNuts.set("0")
    ```             
    8. Now add ```ruby val45=float(varPeaNuts.get())``` on line 776.
    9. In the calculation of temptotal on line 778 add on end (val45*the value of peanut within a bracket).
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
    12. AND THERE YOU GO , NOW RUN THE cafe.py FILE TO SEE THE CHANGES.
    
For deleting any data follow the above procedure in reverse .
GOOD LUCK !!
    
