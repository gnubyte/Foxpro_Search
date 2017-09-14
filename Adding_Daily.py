


import pyodbc

try:
    
    cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
    c = cnxn.cursor()
    c.execute("SELECT Cost FROM Potran01")
    row = c.fetchall()# or c.fetchall for all the results
    if row:
        total = 0
        for listitem in row:
            currentCost =int(listitem[0])
            total = currentCost + total
            
    total = str(total)
    print ("Total of all PO line items this fiscal period: "+total)
except Exception as E:
    print (E)
    
    
    
    
    
import pyodbc

try:
    
    cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
    c = cnxn.cursor()
    c.execute("SELECT Extprice FROM Sotran01")
    row = c.fetchall()# or c.fetchall for all the results
    if row:
        total = 0
        for listitem in row:
            currentCost =int(listitem[0])
            total = currentCost + total
    total = str(total)
    print ("Total of all SOs line items this fiscal period: "+ total)
except Exception as E:
    print (E)
    
    
    
    
    
# ----------------------------------------------------
# daily PO Line item cost
import pyodbc

try:
    
    cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
    c = cnxn.cursor()
    c.execute("SELECT Cost FROM Potran01 WHERE ")
    row = c.fetchall()# or c.fetchall for all the results
    if row:
        total = 0
        for listitem in row:
            currentCost =int(listitem[0])
            total = currentCost + total
            
    total = str(total)
    print ("Total of all PO line items this fiscal period: "+total)
except Exception as E:
    print (E)
    
    
    
    
# ----------------------------------------------------
# daily SO Line item cost
import pyodbc

try:
    
    cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
    c = cnxn.cursor()
    c.execute("SELECT Extprice FROM Sotran01")
    row = c.fetchall()# or c.fetchall for all the results
    if row:
        total = 0
        for listitem in row:
            currentCost =int(listitem[0])
            total = currentCost + total
    total = str(total)
    print ("Total of all SOs line items this fiscal period: "+ total)
except Exception as E:
    print (E)
    
# ----------------------------------------------------
# daily SO Line item cost
import pyodbc

try:
    
    cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
    c = cnxn.cursor()
    c.execute("SELECT Extprice FROM Artran01")
    row = c.fetchall()# or c.fetchall for all the results
    if row:
        total = 0
        for listitem in row:
            currentCost =int(listitem[0])
            total = currentCost + total
    total = str(total)
    print ("Total of all Account Recievable line items this fiscal period: "+ total)
except Exception as E:
    print (E)