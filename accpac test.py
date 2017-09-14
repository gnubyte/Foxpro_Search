import pyodbc


class item_transaction:
    
    def item_transaction_history_search(item):
        try:
            
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            c.execute('''SELECT * from Icytrn01 WHERE icytrn01.item LIKE "'''+item+'''"''')
            row = c.fetchall()# or c.fetchall for all the results
            if row:
                for listitem in row:
                    #print (listitem)
                    Ttranno = listitem[0]
                    #print Ttranno
                    Vpartno = listitem[1]
                    Serial = listitem[2]
                    Loctid = listitem[3]
                    Item = listitem[4]
                    Lotno = listitem[5]
                    Tier = listitem[6]
                    Ref = listitem[7]
                    Trantype = listitem[8]
                    TranDate  = listitem[9]
                    TranStat = listitem[10]
                    TranQty = listitem[11]
                    Listitem = [Ttranno, Vpartno, Serial, Loctid, Item, Lotno, Tier, Ref, Trantype, TranDate, TranStat, TranQty]
                    print (Listitem)
                    #print('Qserial is %s with loctid %s'%(str(listitem[0]), str(listitem[1])))
            else:
                print("No row: value - %s"% (str(row)))
        except Exception as E:
            print (E)
        
def item_transaction_search(item):
    try:
        
        cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
        c = cnxn.cursor()
        c.execute('''SELECT * from Ictran01 WHERE ictran01.item LIKE "'''+item+'''"''')
        row = c.fetchall()# or c.fetchall for all the results
        if row:
            for listitem in row:
                #print (listitem)
                Ttranno = listitem[0]
                #print Ttranno
                Vpartno = listitem[1]
                Serial = listitem[2]
                Loctid = listitem[3]
                Item = listitem[4]
                Lotno = listitem[5]
                Tier = listitem[6]
                Ref = listitem[7]
                Trantype = listitem[8]
                TranDate  = listitem[9]
                TranStat = listitem[10]
                TranQty = listitem[11]
                #print('Qserial is %s with loctid %s'%(str(listitem[0]), str(listitem[1])))
        else:
            print("No row: value - %s"% (str(row)))
    except Exception as ECurrentTransfers:
        print (ECurrentTransfers)


it = item_transaction()
it.item_transaction_history_search()