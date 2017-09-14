# #########
# @Author: Patrick Hastings
# @Date: 8-16-2017
# @Title: Accpac Class
# @Purpose: Accpac data model access
# #########
import pyodbc

class Accpac:
    '''
    Handles Accpac Queries.
    Make sure there is an ODBC with ODBC-32 installed.
    '''
    def SAS(self, Obj):
        '''
        String and Strip tool.
        ------
        1. Creates a string and returns it
        2. Strips string of spaces
        3. Turns * to %
        ------
        Strips an object and converts it to a string.
        Returns a string if all went well.
        Returns 1 if error
        '''
        try:
            Obj = str(Obj)
            Obj = Obj.strip()
            Obj = Obj.replace('*', '%')
            return Obj
        except Exception as StringAndStripError1:
            StringAndStripError1 = str(StringAndStripError1)
            print ("Error while in accpac_class.py code 300: With error message: \n" + StringAndStripError1)
            return 1
    def Summary_Item_Search(self, item):
        '''
        Searches Accpac's items table and retrieves a brief summary
        Intended to list possible desired results
        ------
        Searches table Icitem01
        '''
        try:
            item=self.SAS(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item, Itmdesc, ionhand, Price, Comcode, Ilsale, Ilrecv, Ilordr from icitem01 WHERE TRIM(icitem01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Item
                    Item = self.SAS(listitem[0])
                    SearchResults.append(Item)
                    # Item Description
                    Itmdesc = self.SAS(listitem[1])
                    SearchResults.append(Itmdesc)
                    # Items on Hand
                    Ionhand = self.SAS(listitem[2])
                    SearchResults.append(Ionhand)
                    # Item Price
                    Price = self.SAS(listitem[3])
                    SearchResults.append(Price)
                    # Commodity Code
                    Comcode = self.SAS(listitem[4])
                    SearchResults.append(Comcode)
                    # Item Last Sale Date
                    Ilsale = self.SAS(listitem[5])
                    SearchResults.append(Ilsale)
                    # Item Last Recieved Date
                    Ilrecv = self.SAS(listitem[6])
                    SearchResults.append(Ilrecv)
                    # Item Last Purchased Date
                    Ilordr = self.SAS(listitem[7])
                    SearchResults.append(Ilordr)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as SummaryItemSearchError:
            print (SummaryItemSearchError)
            return 2
    def Summary_Sales_Order_Search(self, sono):
        '''
        Searches Accpac's sales order entry tables
        Intended to list possible desired results
        ------
        Searches table somast01 and soymst01 tables
        '''
        try:
            ResultsHit = 0
            sono=self.SAS(sono)
            sono = "%" + sono + "%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Sono, Sostat, Ponum, Custno, Cshipno, Sodate, Ordate, Sotype, Sotrack from somast01 WHERE TRIM(somast01.sono) LIKE "    '''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                ResultsHit = ResultsHit + 1
                for listitem in rows:
                    SearchResults = []
                    # Sales order number
                    Sono = self.SAS(listitem[0])
                    SearchResults.append(Sono)
                    # Status of Sales order
                    Sostat = self.SAS(listitem[1])
                    SearchResults.append(Sostat)
                    # Purchase Order on SO
                    Ponum = self.SAS(listitem[2])
                    SearchResults.append(Ponum)
                    # Customer
                    Custno = self.SAS(listitem[3])
                    SearchResults.append(Custno)
                    # Store Number/Location Number for this customer
                    Cshipno = self.SAS(listitem[4])
                    SearchResults.append(Cshipno)
                    # Sales Order Date Created
                    Sodate = self.SAS(listitem[5])
                    SearchResults.append(Sodate)
                    # Complete order by this date
                    Ordate = self.SAS(listitem[6])
                    SearchResults.append(Ordate)
                    # Sales Order Type (partial or not)
                    Sotype = self.SAS(listitem[7])
                    SearchResults.append(Sotype)
                    # Sales Order Tracking Number
                    Sotrack = self.SAS(listitem[8])
                    SearchResults.append(Sotrack)
                    #
                    RowsOfResults.append(SearchResults)
                    continue
            else:
                print("No row: value - %s"% (str(rows)))
            # History Search
            c = cnxn.cursor()
            sono = "%" + sono + "%"
            HistorySQL = '''SELECT Sono, Sostat, Ponum, Custno, Cshipno, Sodate, Ordate, Sotype, Sotrack from soymst01 WHERE TRIM(soymst01.sono) LIKE "    '''+sono+'''" '''
            c.execute(HistorySQL)
            HistoryRows = c.fetchall()# or c.fetchall for all the results
            c.close()
            if HistoryRows:
                ResultsHit = ResultsHit + 1
                for HistoryList in HistoryRows:
                    SearchResults = []
                    # Sales order number
                    Sono = self.SAS(HistoryList[0])
                    SearchResults.append(Sono)
                    # Status of Sales order
                    Sostat = self.SAS(HistoryList[1])
                    SearchResults.append(Sostat)
                    # Purchase Order on SO
                    Ponum = self.SAS(HistoryList[2])
                    SearchResults.append(Ponum)
                    # Customer
                    Custno = self.SAS(HistoryList[3])
                    SearchResults.append(Custno)
                    # Store Number/Location Number for this customer
                    Cshipno = self.SAS(HistoryList[4])
                    SearchResults.append(Cshipno)
                    # Sales Order Date Created
                    Sodate = self.SAS(HistoryList[5])
                    SearchResults.append(Sodate)
                    # Complete order by this date
                    Ordate = self.SAS(HistoryList[6])
                    SearchResults.append(Ordate)
                    # Sales Order Type (partial or not)
                    Sotype = self.SAS(HistoryList[7])
                    SearchResults.append(Sotype)
                    # Sales Order Tracking Number
                    Sotrack = self.SAS(HistoryList[8])
                    SearchResults.append(Sotrack)
                    #
                    RowsOfResults.append(SearchResults)
            if ResultsHit > 0:
                return RowsOfResults            
            else:
                return 1
        except Exception as SummarySalesOrderSearch:
            print (SummarySalesOrderSearch)
            return 2
    def Summary_Purchase_Order_Search(self, purno):
        '''
        Searches Accpac's purchase order entry tables, both current and historical
        Intended to list possible desired results
        ------
        Searches table pomast01 and poymst01 tables
        '''
        try:
            ResultsHit = 0
            purno =self.SAS(purno)
            purno = "%" + purno + "%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno, Potype, Postat, Vendno, Puramt, Recamt, Purdate, Reqdate, loctid, Shipvia  from pomast01 WHERE TRIM(pomast01.purno) LIKE "    '''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                ResultsHit = ResultsHit + 1
                for listitem in rows:
                    SearchResults = []
                    # Purchase Order Number
                    Purno = self.SAS(listitem[0])
                    SearchResults.append(Purno)
                    # Purchase Order Type
                    Potype = self.SAS(listitem[1])
                    SearchResults.append(Potype)
                    # Purchase order Status
                    Postat = self.SAS(listitem[2])
                    SearchResults.append(Postat)
                    # Vendor
                    Vendno = self.SAS(listitem[3])
                    SearchResults.append(Vendno)
                    # Purchased Cost Amount
                    Puramt = self.SAS(listitem[4])
                    SearchResults.append(Puramt)
                    # Cost Amount Recieved todate
                    Recamt = self.SAS(listitem[5])
                    SearchResults.append(Recamt)
                    # Purchased on Date
                    Purdate = self.SAS(listitem[6])
                    SearchResults.append(Purdate)
                    # Required Date
                    Reqdate = self.SAS(listitem[7])
                    SearchResults.append(Reqdate)
                    # Location to recieve this inventory to
                    loctid = self.SAS(listitem[8])
                    SearchResults.append(loctid)
                    # Ship via which carrier
                    Shipvia = self.SAS(listitem[9])
                    SearchResults.append(Shipvia)
                    #
                    RowsOfResults.append(SearchResults)
                    continue
            else:
                print("No row: value - %s"% (str(rows)))
            # History Search
            c = cnxn.cursor()
            HistorySQL = '''SELECT Purno, Potype, Postat, Vendno, Puramt, Recamt, Purdate, Reqdate, loctid, Shipvia from poymst01 WHERE TRIM(poymst01.purno) LIKE "'''+purno+'''" '''
            c.execute(HistorySQL)
            HistoryRows = c.fetchall()# or c.fetchall for all the results
            c.close()
            if HistoryRows:
                ResultsHit = ResultsHit + 1
                for HistoryList in HistoryRows:
                    SearchResults = []
                    # Purchase Order Number 
                    Purno = self.SAS(HistoryList[0])
                    SearchResults.append(Purno)
                    # Purchase Order Type
                    Potype = self.SAS(HistoryList[1])
                    SearchResults.append(Potype)
                    # Purchase Order status
                    Postat = self.SAS(HistoryList[2])
                    SearchResults.append(Postat)
                    # Vendor
                    Vendno = self.SAS(HistoryList[3])
                    SearchResults.append(Vendno)
                    # Cash value Purchase Amount
                    Puramt = self.SAS(HistoryList[4])
                    SearchResults.append(Puramt)
                    # Cash value recieved todate
                    Recamt = self.SAS(HistoryList[5])
                    SearchResults.append(Recamt)
                    # Date Purchase Order was placed
                    Purdate = self.SAS(HistoryList[6])
                    SearchResults.append(Purdate)
                    # Date that the purchase order is required
                    Reqdate = self.SAS(HistoryList[7])
                    SearchResults.append(Reqdate)
                    # Location that Purchase order is to be received into
                    loctid = self.SAS(HistoryList[8])
                    SearchResults.append(loctid)
                    # Shipping method of which goods will be delivered
                    Shipvia = self.SAS(HistoryList[9])
                    SearchResults.append(Shipvia)
                    #                    
                    RowsOfResults.append(SearchResults)
            if ResultsHit > 0:
                return RowsOfResults            
            else:
                return 1
        except Exception as SummaryPurchaseOrderError:
            print (SummaryPurchaseOrderError)
            return 2    
    def Open_Sales_Order_Search(self, item):
        '''
        Searches current fiscal period's open sales orders
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT custno, sono, qtyord, qtyshp, rqdate from Sotran01 WHERE TRIM(sotran01.item) LIKE "'''+item+'''" AND sostat = '' '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    custno = self.SAS(listitem[0])
                    SearchResults.append(custno)
                    #
                    sono = self.SAS(listitem[1])
                    SearchResults.append(sono)
                    #
                    qtyord = self.SAS(listitem[2])
                    SearchResults.append(qtyord)
                    #
                    qtyshp = self.SAS(listitem[3])
                    SearchResults.append(qtyshp)
                    #
                    rqdate = self.SAS(listitem[4])
                    SearchResults.append(rqdate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as OpenSOSError:
            print (OpenSOSError)
            return 2
            
    def Sales_History_Order_Search(self, item):
        '''
        Searches the sales order line item history file - soytrn and returns rows
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT custno, sono, qtyord, qtyshp, shipdate, Sostat, Sotype, Serial from Soytrn01 WHERE TRIM(soytrn01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    #
                    custno = self.SAS(listitem[0])
                    SearchResults.append(custno)
                    #
                    sono = self.SAS(listitem[1])
                    SearchResults.append(sono)
                    #
                    qtyord = self.SAS(listitem[2])
                    SearchResults.append(qtyord)
                    #
                    qtyshp = self.SAS(listitem[3])
                    SearchResults.append(qtyshp)
                    #
                    shipdate = self.SAS(listitem[4])
                    SearchResults.append(shipdate)
                    #
                    rqdate = self.SAS(listitem[4])
                    SearchResults.append(rqdate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SO_History:
            print (Error_SO_History)
            return 2
            
    def Open_Purchase_Orders_Search(self, item):
        '''
        Searches current fiscal period for open purchase orders
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT custno, sono, qtyord, qtyshp, shipdate, Sostat, Sotype, Serial from Soytrn01 WHERE TRIM(soytrn01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    custno = listitem[0]
                    custno = self.SAS(custno)
                    SearchResults.append(custno)
                    #
                    sono = listitem[1]
                    sono = self.SAS(sono)
                    SearchResults.append(sono)
                    #
                    qtyord = listitem[2]
                    qtyord = self.SAS(qtyord)
                    SearchResults.append(qtyord)
                    #
                    qtyshp = listitem[3]
                    qtyshp = self.SAS(qtyshp)
                    SearchResults.append(qtyshp)
                    #
                    rqdate = listitem[4]
                    SearchResults.append(rqdate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SO_History:
            print (Error_SO_History)
            return 2
    
    def Purchase_Search(self, item):
        '''
        Search for open purchase ordesr in active period
        ------
        8-22-2017: Updated for Rows Of Results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT purno,vendno,cost, qtyord, qtyrec, postat, reqdate from potran01 WHERE TRIM(potran01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    purno = listitem[0]
                    purno = self.SAS(purno)
                    SearchResults.append(purno)
                    #
                    vendno = listitem[1]
                    vendno = self.SAS(vendno)
                    SearchResults.append(vendno)
                    #
                    cost = listitem[2]
                    cost = self.SAS(cost)
                    SearchResults.append(cost)
                    #
                    qtyord = listitem[3]
                    qtyord = self.SAS(qtyord)
                    SearchResults.append(qtyord)
                    #
                    qtyrec = listitem[4]
                    qtyrec = self.SAS(qtyrec)
                    SearchResults.append(qtyrec)
                    #
                    postat = listitem[5]
                    postat = self.SAS(postat)
                    SearchResults.append(postat)
                    #
                    reqdate = listitem[6]
                    SearchResults.append(reqdate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_PO_Active:
            print (Error_PO_Active)
            return 2        
        
    def Purchase_History_Search(self, item):
        '''
        Search for purchase history
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT purno,vendno,cost, qtyord, qtyrec, postat, recdate from poytrn01 WHERE TRIM(poytrn01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    #
                    purno = listitem[0]
                    purno = self.SAS(purno)
                    SearchResults.append(purno)
                    #
                    vendno = listitem[1]
                    vendno = self.SAS(vendno)
                    SearchResults.append(vendno)
                    #
                    cost = listitem[2]
                    cost = self.SAS(cost)
                    SearchResults.append(cost)
                    #
                    qtyord = listitem[3]
                    qtyord = self.SAS(qtyord)
                    SearchResults.append(qtyord)
                    #
                    qtyrec = listitem[4]
                    qtyrec = self.SAS(qtyrec)
                    SearchResults.append(qtyrec)
                    #
                    postat = listitem[5]
                    postat = self.SAS(postat)
                    SearchResults.append(postat)
                    #
                    reqdate = listitem[6]
                    SearchResults.append(reqdate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_PO_Active:
            print (Error_PO_Active)
            return 2        
    def Item_Search(self, item):
        '''
        Search for current inventory in iciqty for items on hand
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item,Loctid,Qonhand,Qsoaloc,Qstore,Qbin, Qserial from iciqty01 WHERE TRIM(iciqty01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    Item = listitem[0]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    #
                    Loctid = listitem[1]
                    Loctid = self.SAS(Loctid)
                    SearchResults.append(Loctid)
                    #
                    Qonhand = listitem[2]
                    Qonhand = self.SAS(Qonhand)
                    SearchResults.append(Qonhand)
                    #
                    Qsoaloc = listitem[3]
                    Qsoaloc = self.SAS(Qsoaloc)
                    SearchResults.append(Qsoaloc)
                    #
                    Qstore = listitem[4]
                    Qstore = self.SAS(Qstore)
                    SearchResults.append(Qstore)
                    #
                    Qbin = listitem[5]
                    Qbin = self.SAS(Qbin)
                    SearchResults.append(Qbin)
                    #
                    Qserial = listitem[6]
                    Qserial = self.SAS(Qserial)
                    SearchResults.append(Qserial)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_item_Active:
            print (Error_item_Active)
            return 2     
    def Items_by_Location_Search(self, loctid):
        '''
        Search for current inventory in iciqty for items on hand by location
        '''
        try:
            loctid = self.SAS(loctid)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item,Loctid,Qonhand,Qsoaloc,Qstore,Qbin, Qserial from iciqty01 WHERE TRIM(iciqty01.Loctid) LIKE "'''+loctid+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    Item = listitem[0]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    #
                    Loctid = listitem[1]
                    Loctid = self.SAS(Loctid)
                    SearchResults.append(Loctid)
                    #
                    Qonhand = listitem[2]
                    Qonhand = self.SAS(Qonhand)
                    SearchResults.append(Qonhand)
                    #
                    Qsoaloc = listitem[3]
                    Qsoaloc = self.SAS(Qsoaloc)
                    SearchResults.append(Qsoaloc)
                    #
                    Qstore = listitem[4]
                    Qstore = self.SAS(Qstore)
                    SearchResults.append(Qstore)
                    #
                    Qbin = listitem[5]
                    Qbin = self.SAS(Qbin)
                    SearchResults.append(Qbin)
                    #
                    Qserial = listitem[6]
                    Qserial = self.SAS(Qserial)
                    SearchResults.append(Qserial)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_itemByLoc_Active:
            print (Error_itemByLoc_Active)
            return 2         
    
    def Item_Header_Search(self, item):
        '''
        Search for current inventory in icitem for items on hand
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item,Itmdesc, Comcode, Plinid,Altitm1,Altitm2, Fru1, Fru2, Fru3, Fru4, Fru5,Ionhand,ilsale, ilrecv, ilpcnt, ilordr, Price from icitem01 WHERE TRIM(icitem01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Item 
                    Item = self.SAS(listitem[0])
                    SearchResults.append(Item)
                    # Item Description
                    Itmdesc = self.SAS(listitem[1])
                    SearchResults.append(Itmdesc)
                    # Item Commodity Code
                    Comcode = self.SAS(listitem[2])
                    SearchResults.append(Comcode)
                    # Product Code tree level
                    Plinid = self.SAS(listitem[3])
                    SearchResults.append(Plinid)
                    # Alternate FRU number 1
                    Altitm1 = self.SAS(listitem[4])
                    SearchResults.append(Altitm1)
                    # Alternate FRU number 2
                    Altitm2 = self.SAS(listitem[5])
                    SearchResults.append(Altitm2)
                    # Alternate part number 1
                    Fru1 = self.SAS(listitem[6])
                    SearchResults.append(Fru1)
                    # Alternate Part Number 2
                    Fru2 = self.SAS(listitem[7])
                    SearchResults.append(Fru2)
                    # Alternate Part Number 3
                    Fru3 = self.SAS(listitem[8])
                    SearchResults.append(Fru3)
                    # Alternate Part Number 4
                    Fru4 = self.SAS(listitem[9])
                    SearchResults.append(Fru4)
                    # Alternate Part Number 5
                    Fru5 = self.SAS(listitem[10])
                    SearchResults.append(Fru5)
                    # Inventory on hand
                    Ionhand = self.SAS(listitem[11])
                    SearchResults.append(Ionhand)
                    # Last Sale Date
                    LastSale = self.SAS(listitem[12])
                    SearchResults.append(LastSale)
                    # Last sale recieval date
                    LastReceival = self.SAS(listitem[13])
                    SearchResults.append(LastReceival)
                    # Last Cycle Count
                    LastCycleCount = self.SAS(listitem[14])
                    SearchResults.append(LastCycleCount)
                    # Last purchase order date
                    LastPO = self.SAS(listitem[15])
                    SearchResults.append(LastPO)
                    # Item Price
                    Price = self.SAS(listitem[16])
                    SearchResults.append(Price)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_item_Active:
            print (Error_item_Active)
            return 2   

    def Item_Transaction_Search(self, item):
        '''
        Search for current fiscal period, Item transaction  file for the current fiscal period
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Ttranno,Serial,Loctid,Item,Tier,Ref,Trantyp, Tstat, Tqty, Tcost, Orgno, Docno, Tstore,Tbin  from ictran01 WHERE TRIM(ictran01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    #Transaction Number
                    Tranno = listitem[0]
                    Tranno = self.SAS(Tranno)
                    SearchResults.append(Tranno)
                    # Serial Number
                    Serial = listitem[1]
                    Serial = self.SAS(Serial)
                    SearchResults.append(Serial)
                    #Location ID
                    Loctid = listitem[2]
                    Loctid = self.SAS(Loctid)
                    SearchResults.append(Loctid)
                    # Item
                    Item = listitem[3]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    # Cost - Tier
                    CTier = listitem[4]
                    CTier = self.SAS(CTier)
                    SearchResults.append(CTier)
                    # Reference Field
                    Ref = listitem[5]
                    Ref = self.SAS(Ref)
                    SearchResults.append(Ref)
                    # Transaction Type
                    Trantyp = listitem[6]
                    Trantyp = self.SAS(Trantyp)
                    SearchResults.append(Trantyp)
                    # Transaction Status
                    Transtat = listitem[7]
                    Transtat = self.SAS(Transtat)
                    SearchResults.append(Transtat)
                    # Transaction Quantity
                    TranQty = listitem[8]
                    TranQty = self.SAS(TranQty)
                    SearchResults.append(TranQty)
                    # Transaction Cost
                    Trancost = listitem[9]
                    Trancost = self.SAS(Trancost)
                    SearchResults.append(Trancost)
                    # Organization (Location?)
                    Orgno = listitem[10]
                    Orgno = self.SAS(Orgno)
                    SearchResults.append(Orgno)
                    # Document Number AKA Purchase Order
                    Docno = listitem[11]
                    Docno = self.SAS(Docno)
                    SearchResults.append(Docno)
                    # Transaction Store AKA Rowbay
                    Tstore = self.SAS(listitem[12])
                    SearchResults.append(Tstore)
                    # Transaction Bin AKA bin
                    Tbin  = listitem[13]
                    SearchResults.append(Tbin)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_item_Cost:
            print (Error_item_Cost)
            return 2      
    def Item_Transaction_History_Search(self, item):
        '''
        Search for current fiscal period, Item transaction history file
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Ttranno,Serial,Loctid,Item,Tier,Ref,Trantyp, Tdate, Tstat, Tqty, Tcost, Price, Orgno, Docno, Tstore,Tbin  from icytrn01 WHERE TRIM(icytrn01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    #Transaction Number
                    Tranno = self.SAS(listitem[0])
                    SearchResults.append(Tranno)
                    # Serial Number
                    Serial = self.SAS(listitem[1])
                    SearchResults.append(Serial)
                    #Location ID
                    Loctid = self.SAS(listitem[2])
                    SearchResults.append(Loctid)
                    # Item
                    Item = self.SAS(listitem[3])
                    SearchResults.append(Item)
                    # Cost - Tier
                    CTier = self.SAS(listitem[4])
                    SearchResults.append(CTier)
                    # Reference Field
                    Ref = self.SAS(listitem[5])
                    SearchResults.append(Ref)
                    # Transaction Type
                    Trantyp = self.SAS(listitem[6])
                    SearchResults.append(Trantyp)
                    # Transaction Date
                    Tdate = self.SAS(listitem[7])
                    SearchResults.append(Tdate)
                    # Transaction Status
                    Transtat = self.SAS(listitem[8])
                    SearchResults.append(Transtat)
                    # Transaction Quantity
                    TranQty = self.SAS(listitem[9])
                    SearchResults.append(TranQty)
                    # Transaction Cost
                    Trancost = self.SAS(listitem[10])
                    SearchResults.append(Trancost)
                    # Price
                    Price = self.SAS(listitem[11])
                    SearchResults.append(Price)
                    # Organization (Location?)
                    Orgno = self.SAS(listitem[12])
                    SearchResults.append(Orgno)
                    # Document Number AKA Purchase Order
                    Docno = self.SAS(listitem[13])
                    SearchResults.append(Docno)
                    # Transaction Store AKA Rowbay
                    Tstore = self.SAS(listitem[14])
                    SearchResults.append(Tstore)
                    # Transaction Bin AKA bin
                    Tbin  = self.SAS(listitem[15])
                    SearchResults.append(Tbin)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_item_history_Cost:
            print (Error_item_history_Cost)
            return 2              
    def Item_Location_Search(self, item):
        '''
        Search for current fiscal period, Item location table
        Items at location
        ------
        8-22-2017: Updated for rows of results
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item,Loctid, Lonhand,Lonordr,Orderpt,Ordqty,Lsale,Lrecv from iciloc01 WHERE TRIM(iciloc01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Item Number
                    Item = self.SAS(listitem[0])
                    SearchResults.append(Item)
                    # Inventory Location
                    Loctid = self.SAS(listitem[1])
                    SearchResults.append(Loctid)
                    # Items on Hand
                    Lonhand = self.SAS(listitem[2])
                    SearchResults.append(Lonhand)
                    # Quantity of Items currently on Order
                    Lonordr = self.SAS(listitem[3])
                    SearchResults.append(Lonordr)
                    # Order Point 
                    Orderpt = self.SAS(listitem[4])
                    SearchResults.append(Orderpt)
                    # Ordered Quantity
                    Ordqty = self.SAS(listitem[5])
                    SearchResults.append(Ordqty)
                    # Date of Last sale of item at this location
                    Lsale = listitem[6]
                    SearchResults.append(Lsale)
                    # Date of Last recieved into this location
                    Lrecv = listitem[7]
                    SearchResults.append(Lrecv)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_Item_Location:
            print (Error_Item_Location)
            return 2              

    def Item_Cost_Search(self, item):
        '''
        Search for current inventory in iciqty for items on hand
        ------
        8-22-2017: Updated for rows of rows
        '''
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Item,Loctid,Tier,Conhand,Cost,Adduser from iccost01 WHERE TRIM(iccost01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    #
                    Item = listitem[0]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    #
                    Loctid = listitem[1]
                    Loctid = self.SAS(Loctid)
                    SearchResults.append(Loctid)
                    #
                    Tier = listitem[2]
                    Tier = self.SAS(Tier)
                    SearchResults.append(Tier)
                    #
                    Conhand = listitem[3]
                    Conhand = self.SAS(Conhand)
                    SearchResults.append(Conhand)
                    #
                    Cost = listitem[4]
                    Cost = self.SAS(Cost)
                    SearchResults.append(Cost)
                    #
                    Adduser = listitem[5]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_item_Cost:
            print (Error_item_Cost)
            return 2      
#Sales Order block
    def Sales_Order_Header_Current_Search(self, sono):
        '''
        Searches Accpac's current fiscal period for sales orders.
        Searches the Somast01 table in accpac
        '''
        try:
            sono=self.SAS(sono)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Sono,Custno,Sodate,Ordate,Shipvia,Cshipno, Pterms, Ordamt, Shpamt, Ponum, Sostat, Sotype, Ref, Sotrack, notify, trackemail  from somast01 WHERE TRIM(somast01.sono) LIKE "     '''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Sales order Number
                    Sono = listitem[0]
                    Sono = self.SAS(Sono)
                    SearchResults.append(Sono)
                    # Location ID
                    Custno = listitem[1]
                    Custno = self.SAS(Custno)
                    SearchResults.append(Custno)
                    # Sales order date
                    Sodate = listitem[2]
                    SearchResults.append(Sodate)
                    # Order ship date
                    Ordate = listitem[3]
                    SearchResults.append(Ordate)
                    # Ship Via
                    Shipvia = listitem[4]
                    Shipvia = self.SAS(Shipvia)
                    SearchResults.append(Shipvia)
                    # Cshipno - Store Number or Location number
                    Cshipno = listitem[5]
                    Cshipno = self.SAS(Cshipno)
                    SearchResults.append(Cshipno)
                    # Pay terms 
                    Pterms = listitem[6]
                    Pterms = self.SAS(Pterms)
                    SearchResults.append(Pterms)
                    # Ordered Amount
                    Ordamt = listitem[7]
                    Ordamt = self.SAS(Ordamt)
                    SearchResults.append(Ordamt)
                    #Shipped Amount
                    Shpamt = listitem[8]
                    Shpamt = self.SAS(Shpamt)
                    SearchResults.append(Shpamt)
                    # Purchase Order Number
                    Ponum = listitem[9]
                    Ponum = self.SAS(Ponum)
                    SearchResults.append(Ponum)
                    # Sales Order Status
                    Sostat = listitem[10]
                    Sostat = self.SAS(Sostat)
                    SearchResults.append(Sostat)
                    # Sales Order Type
                    Sotype = listitem[11]
                    Sotype = self.SAS(Sotype)
                    SearchResults.append(Sotype)                    
                    # References - Usually PO #
                    Ref = listitem[12]
                    Ref = self.SAS(Ref)
                    SearchResults.append(Ref)
                    # Sales Order Tracking Number
                    Sotrack = listitem[13]
                    Sotrack = self.SAS(Sotrack)
                    SearchResults.append(Sotrack)                    
                    # Notify status
                    notify = listitem[14]
                    notify = self.SAS(notify)
                    SearchResults.append(notify)
                    # Track email
                    trackemail = listitem[15]
                    trackemail = self.SAS(trackemail)
                    SearchResults.append(trackemail)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOMAST_Search:
            print (Error_SOMAST_Search)
            return 2              
    def Sales_Order_Comment_Current_Search(self, sono):
        '''
        Searches Accpac's current sales order comments in fiscal period.
        Searches the Socomm01 table in accpac
        '''
        try:
            sono=self.SAS(sono)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Sono,Comment,Adduser,Adddate from socomm01 WHERE TRIM(socomm01.sono) LIKE "     '''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Sales order Number
                    Sono = listitem[0]
                    Sono = self.SAS(Sono)
                    SearchResults.append(Sono)
                    # Comment
                    Comment = listitem[1]
                    Comment = self.SAS(Comment)
                    SearchResults.append(Comment)
                    # Add user
                    Adduser = listitem[2]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Add date
                    Adddate = listitem[3]
                    SearchResults.append(Adddate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOCOMM_Search:
            print (Error_SOCOMM_Search)
            return 2
    def Sales_Order_Address_Current_Search(self, sono):
        '''
        Searches Accpac's current sales order address line in fiscal period.
        Searches the Soaddr01 table in accpac
        '''
        try:
            sono=self.SAS(sono)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Custno,Sono,Company,Address1,Address2, Address3,City, State, Zip, Cshipno, Adduser,Adddate  from soaddr01 WHERE TRIM(soaddr01.sono) LIKE "     '''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Customer
                    Custno = listitem[0]
                    Custno = self.SAS(Custno)
                    SearchResults.append(Custno)
                    # Sales order number
                    Sono = listitem[1]
                    Sono = self.SAS(Sono)
                    SearchResults.append(Sono)
                    # Company
                    Company = listitem[2]
                    Company = self.SAS(Company)
                    SearchResults.append(Company)
                    # Address 1
                    Addr1 = listitem[3]
                    Addr1 = self.SAS(Addr1)
                    SearchResults.append(Addr1)
                    # Address 2
                    Addr2 = listitem[4]
                    Addr2 = self.SAS(Addr2)
                    SearchResults.append(Addr2)
                    # Address 3
                    Addr3 = listitem[5]
                    Addr3 = self.SAS(Addr3)
                    SearchResults.append(Addr3)
                    # City
                    City = listitem[6]
                    City = self.SAS(City)
                    SearchResults.append(City)
                    # State
                    State = listitem[7]
                    State = self.SAS(State)
                    SearchResults.append(State)
                    # Zip
                    Zip = listitem[8]
                    Zip = self.SAS(Zip)
                    SearchResults.append(Zip)
                    # Customer Ship number - location number
                    Cshipno = listitem[9]
                    Cshipno = self.SAS(Cshipno)
                    SearchResults.append(Cshipno)
                    # Add user
                    Adduser = listitem[10]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Add date
                    Adddate = listitem[11]
                    SearchResults.append(Adddate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOADDR_Search:
            print (Error_SOADDR_Search)
            return 2
    def Sales_Order_Address_History_Search(self, sono):
        '''
        Searches Accpac's sales order address line in  historical fiscal records.
        Searches the Soyadr01 table in accpac
        '''
        try:
            sono="%" +self.SAS(sono) + "%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Custno,Sono,Company,Address1,Address2, Address3,City, State, Zip, Cshipno, Adduser,Adddate  from soyadr01 WHERE TRIM(soyadr01.sono) LIKE "'''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Customer
                    Custno = listitem[0]
                    Custno = self.SAS(Custno)
                    SearchResults.append(Custno)
                    # Sales order number
                    Sono = listitem[1]
                    Sono = self.SAS(Sono)
                    SearchResults.append(Sono)
                    # Company
                    Company = listitem[2]
                    Company = self.SAS(Company)
                    SearchResults.append(Company)
                    # Address 1
                    Addr1 = listitem[3]
                    Addr1 = self.SAS(Addr1)
                    SearchResults.append(Addr1)
                    # Address 2
                    Addr2 = listitem[4]
                    Addr2 = self.SAS(Addr2)
                    SearchResults.append(Addr2)
                    # Address 3
                    Addr3 = listitem[5]
                    Addr3 = self.SAS(Addr3)
                    SearchResults.append(Addr3)
                    # City
                    City = listitem[6]
                    City = self.SAS(City)
                    SearchResults.append(City)
                    # State
                    State = listitem[7]
                    State = self.SAS(State)
                    SearchResults.append(State)
                    # Zip
                    Zip = listitem[8]
                    Zip = self.SAS(Zip)
                    SearchResults.append(Zip)
                    # Customer Ship number - location number
                    Cshipno = listitem[9]
                    Cshipno = self.SAS(Cshipno)
                    SearchResults.append(Cshipno)
                    # Add user
                    Adduser = listitem[10]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Add date
                    Adddate = listitem[11]
                    SearchResults.append(Adddate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOADDR_History_Search:
            print (Error_SOADDR_History_Search)
            return 2    
    
    def Sales_Order_Item_Current_Search(self, sono):
        '''
        Searches Accpac's current sales order line items in current fiscal period.
        ------
        Searches the Sotran01 table in accpac
        '''
        try:
            sono=self.SAS(sono)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Sono,Custno,Item,Descrip ,Cost, Price, Ordate,Qtyord, Qtyshp, Cost, Price, Extprice  from sotran01 WHERE TRIM(sotran01.sono) LIKE "     '''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Sales Order Number
                    Sono = listitem[0]
                    Sono = self.SAS(Sono)
                    SearchResults.append(Sono)
                    # Customer
                    Custno = listitem[1]
                    Custno = self.SAS(Custno)
                    SearchResults.append(Custno)
                    # Company
                    Item = listitem[2]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    # Description
                    Descrip = listitem[3]
                    Descrip = self.SAS(Descrip)
                    SearchResults.append(Descrip)
                    # Cost
                    Cost = listitem[4]
                    Cost = self.SAS(Cost)
                    SearchResults.append(Cost)
                    # Price
                    Price = listitem[5]
                    Price = self.SAS(Price)
                    SearchResults.append(Price)
                    # Order needs to deliver by date
                    Ordate = listitem[6]
                    Ordate = self.SAS(Ordate)
                    SearchResults.append(Ordate)
                    # Quantity of line item order
                    Qtyord = listitem[7]
                    Qtyord = self.SAS(Qtyord)
                    SearchResults.append(Qtyord)
                    # Quantity shipped of line item on order
                    Qtyshp = listitem[8]
                    Qtyshp = self.SAS(Qtyshp)
                    SearchResults.append(Qtyshp)
                    # Cost of each line item
                    Cost = listitem[9]
                    Cost = self.SAS(Cost)
                    SearchResults.append(Cost)
                    # Price of the line item
                    Price = self.SAS(listitem[10])
                    SearchResults.append(Price)
                    # Add date
                    Extprice = self.SAS(listitem[11])
                    SearchResults.append(Extprice)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOTRAN_Search:
            print (Error_SOTRAN_Search)
            return 2        
    def Sales_Order_Header_History_Search(self, sono):
        '''
        Searches Accpac's history sales order lines in historical fiscal periods.
        ------
        Searches the Soymst01 table in accpac
        '''
        try:
            sono="%"+ self.SAS(sono)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Sono,Custno,Ponum, Sostat, Ordamt ,Shpamt, Sodate, Ordate,Ref, sotrack from soymst01 WHERE TRIM(soymst01.sono) LIKE "'''+sono+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Sales Order Number
                    Sono = self.SAS(listitem[0])
                    SearchResults.append(Sono)
                    # Customer
                    Custno = listitem[1]
                    Custno = self.SAS(Custno)
                    SearchResults.append(Custno)
                    # Purchase Order Number
                    Ponum = self.SAS(listitem[2])
                    SearchResults.append(Ponum)
                    # Sales Order status
                    Sostat = self.SAS(listitem[3])
                    SearchResults.append(Sostat)
                    # Order Amount
                    Ordamt = self.SAS(listitem[4])
                    SearchResults.append(Ordamt)
                    # Shipped Amount
                    Shpamt = self.SAS(listitem[5])
                    SearchResults.append(Shpamt)
                    # Sales Order Date
                    Sodate = self.SAS(listitem[6])
                    SearchResults.append(Sodate)
                    # Order to sell by date
                    Ordate = self.SAS(listitem[7])
                    SearchResults.append(Ordate)
                    # References Field in sales order
                    Ref = self.SAS(listitem[8])
                    SearchResults.append(Ref)
                    # Sales Order Tracking Number
                    Sotrack = self.SAS(listitem[8])
                    SearchResults.append(Sotrack)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_SOYMST_Search:
            print (Error_SOYMST_Search)
            return 2            
        
    def Purchase_Order_Current_Search(self, purno):
        '''
        Search for purchase orders in current fiscal period
        '''
        try:
            purno = self.SAS(purno)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno,Vendno,Company, Puramt, Purdate,Recamt,Reqdate, Loctid,Shipvia, Remarks, Potype, Postat, Adduser, Adddate  from pomast01 WHERE TRIM(pomast01.Purno) LIKE "     '''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Purchase Number
                    Purno = listitem[0]
                    Purno = self.SAS(Purno)
                    SearchResults.append(Purno)
                    # Vendor
                    Vendno = listitem[1]
                    Vendno = self.SAS(Vendno)
                    SearchResults.append(Vendno)
                    # Company
                    Company = listitem[2]
                    Company = self.SAS(Company)
                    SearchResults.append(Company)
                    # Purchase Amount
                    Puramt = listitem[3]
                    Puramt = self.SAS(Puramt)
                    SearchResults.append(Puramt)
                    # Purchased Date
                    Purdate = listitem[4]
                    Purdate= self.SAS(Purdate)
                    SearchResults.append(Purdate)
                    # Recieved Amount of cash on inventory to date
                    Recamt = listitem[5]
                    Recamt = self.SAS(Recamt)
                    SearchResults.append(Recamt)
                    # Required date
                    Reqdate = listitem[6]
                    Reqdate = self.SAS(Reqdate)
                    SearchResults.append(Reqdate)
                    # Location ID
                    Loctid = listitem[7]
                    Loctid = self.SAS(Loctid)
                    SearchResults.append(Loctid)
                    # Shipping Method
                    Shipvia = listitem[8]
                    Shipvia = self.SAS(Shipvia)
                    SearchResults.append(Shipvia)
                    # Remarks- SOPO generated?
                    Remarks = listitem[9]
                    Remarks = self.SAS(Remarks)
                    SearchResults.append(Remarks)
                    # Purchase Order Type
                    Potype = listitem[10]
                    Potype = self.SAS(Potype)
                    SearchResults.append(Potype)
                    # Purchase Order Status current 
                    Postat = listitem[11]
                    Postat = self.SAS(Postat)
                    SearchResults.append(Postat)
                    # Added by user
                    Adduser = listitem[12]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Added on Date
                    Adddate = listitem[13]
                    Adddate = self.SAS(Adddate)
                    SearchResults.append(Adddate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_POMAST01:
            print (Error_POMAST01)
            return 2
    def Purchase_Order_Current_Items(self, purno):
        '''
        Searches the current fiscal period for Accpac Purchase Order Line Items
        ------
        Searches Table Potran01
        '''
        try:
            purno = self.SAS(purno)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno,Item,Descrip,Cost, Qtyord,Qtyrec,Purdate,Extcost,Recdate, Reqdate, Itmacct, Forloct, Postat, Potype, Lineno from potran01 WHERE TRIM(potran01.Purno) LIKE "     '''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Purchase Number
                    Purno = listitem[0]
                    Purno = self.SAS(Purno)
                    SearchResults.append(Purno)
                    # Line Item
                    Item = listitem[1]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    # Description
                    Descrip = listitem[2]
                    Descrip = self.SAS(Descrip)
                    SearchResults.append(Descrip)
                    # Cost of line item
                    Cost = listitem[3]
                    Cost = self.SAS(Cost)
                    SearchResults.append(Cost)
                    # Quantity Ordered
                    Qtyord= listitem[4]
                    Qtyord = self.SAS(Qtyord)
                    SearchResults.append(Qtyord)
                    # Quantity Recieved todate
                    Qtyrec = listitem[5]
                    Qtyrec = self.SAS(Qtyrec)
                    SearchResults.append(Qtyrec)
                    # Purchased Date
                    Purdate = listitem[6]
                    Purdate = self.SAS(Purdate)
                    SearchResults.append(Purdate)
                    # Extended line item cost
                    Extcost = listitem[7]
                    Extcost = self.SAS(Extcost)
                    SearchResults.append(Extcost)
                    # Received Date
                    Recdate = listitem[8]
                    Recdate = self.SAS(Recdate)
                    SearchResults.append(Recdate)
                    # Required Date of arrival
                    Reqdate = listitem[9]
                    Reqdate = self.SAS(Reqdate)
                    SearchResults.append(Reqdate)
                    # Item Account - bill to this account
                    Itmacct = listitem[10]
                    Itmacct = self.SAS(Itmacct)
                    SearchResults.append(Itmacct)
                    # Recieve to location
                    Forloct = listitem[11]
                    Forloct = self.SAS(Forloct)
                    SearchResults.append(Forloct)
                    # Purchase Order Status
                    Postat = listitem[12]
                    Postat = self.SAS(Postat)
                    SearchResults.append(Postat)
                    # Purchase Order Type
                    Potype = listitem[13]
                    Potype = self.SAS(Potype)
                    SearchResults.append(Potype)
                    # Line Number
                    Lineno = listitem[14]
                    Lineno = self.SAS(Lineno)
                    SearchResults.append(Lineno)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_POTRAN01:
            print (Error_POTRAN01)
            return 2        
    
    def Purchase_Order_History_Items(self, purno):
        '''
        Searches the historical fiscal records for Accpac Purchase Order Line Items
        ------
        Searches Table Poytrn01
        '''
        try:
            purno = "%"+self.SAS(purno)+"%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno,Item,Descrip,Cost, Qtyord,Qtyrec,Purdate,Extcost,Recdate, Reqdate, Itmacct, Forloct, Postat, Potype, Lineno from poytrn01 WHERE TRIM(poytrn01.Purno) LIKE "'''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Purchase Number
                    Purno = listitem[0]
                    Purno = self.SAS(Purno)
                    SearchResults.append(Purno)
                    # Line Item
                    Item = listitem[1]
                    Item = self.SAS(Item)
                    SearchResults.append(Item)
                    # Description
                    Descrip = listitem[2]
                    Descrip = self.SAS(Descrip)
                    SearchResults.append(Descrip)
                    # Cost of line item
                    Cost = listitem[3]
                    Cost = self.SAS(Cost)
                    SearchResults.append(Cost)
                    # Quantity Ordered
                    Qtyord= listitem[4]
                    Qtyord = self.SAS(Qtyord)
                    SearchResults.append(Qtyord)
                    # Quantity Recieved todate
                    Qtyrec = listitem[5]
                    Qtyrec = self.SAS(Qtyrec)
                    SearchResults.append(Qtyrec)
                    # Purchased Date
                    Purdate = listitem[6]
                    Purdate = self.SAS(Purdate)
                    SearchResults.append(Purdate)
                    # Extended line item cost
                    Extcost = listitem[7]
                    Extcost = self.SAS(Extcost)
                    SearchResults.append(Extcost)
                    # Received Date
                    Recdate = listitem[8]
                    Recdate = self.SAS(Recdate)
                    SearchResults.append(Recdate)
                    # Required Date of arrival
                    Reqdate = listitem[9]
                    Reqdate = self.SAS(Reqdate)
                    SearchResults.append(Reqdate)
                    # Item Account - bill to this account
                    Itmacct = listitem[10]
                    Itmacct = self.SAS(Itmacct)
                    SearchResults.append(Itmacct)
                    # Recieve to location
                    Forloct = listitem[11]
                    Forloct = self.SAS(Forloct)
                    SearchResults.append(Forloct)
                    # Purchase Order Status
                    Postat = listitem[12]
                    Postat = self.SAS(Postat)
                    SearchResults.append(Postat)
                    # Purchase Order Type
                    Potype = listitem[13]
                    Potype = self.SAS(Potype)
                    SearchResults.append(Potype)
                    # Line Number
                    Lineno = listitem[14]
                    Lineno = self.SAS(Lineno)
                    SearchResults.append(Lineno)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_POYTRN01:
            print (Error_POYTRN01)
            return 2            
    
    def Purchase_Order_Current_Address(self, purno):
        '''
        Searches the current fiscal period for Accpac Purchase Order Address fields pertaining to the order
        ------
        Searches Table Poaddr01
        '''
        try:
            purno = self.SAS(purno)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno, Tocompany, Toaddr1, Toaddr2, Toaddr3, Shcompany, Shaddr1, Shaddr2, Shaddr3, Adduser, Adddate, Tozip, Tostate, Tocity from poaddr01 WHERE TRIM(poaddr01.Purno) LIKE "     '''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Purchase Number
                    Purno = listitem[0]
                    Purno = self.SAS(Purno)
                    SearchResults.append(Purno)
                    # Remit To Company
                    Tocompany = listitem[1]
                    Tocompany = self.SAS(Tocompany)
                    SearchResults.append(Tocompany)
                    # Remit To Address 1
                    Toaddr1 = listitem[2]
                    Toaddr1 = self.SAS(Toaddr1)
                    SearchResults.append(Toaddr1)
                    # Remit To address2
                    Toaddr2 = listitem[3]
                    Toaddr2 = self.SAS(Toaddr2)
                    SearchResults.append(Toaddr2)
                    # Remit To address 3
                    Toaddr3 = listitem[4]
                    Toaddr3 = self.SAS(Toaddr3)
                    SearchResults.append(Toaddr3)
                    # Destination Ship company
                    Shcompany = listitem[5]
                    Shcompany = self.SAS(Shcompany)
                    SearchResults.append(Shcompany)
                    # Destination Ship address 1
                    Shaddr1 = listitem[6]
                    Shaddr1 = self.SAS(Shaddr1)
                    SearchResults.append(Shaddr1)
                    # Destination Ship address 2
                    Shaddr2 = listitem[7]
                    Shaddr2 = self.SAS(Shaddr2)
                    SearchResults.append(Shaddr2)
                    # Destination Ship address 3
                    Shaddr3 = listitem[8]
                    Shaddr3 = self.SAS(Shaddr3)
                    SearchResults.append(Shaddr3)
                    # added by user
                    Adduser = listitem[9]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Added on date
                    Adddate = listitem[10]
                    Adddate = self.SAS(Adddate)
                    SearchResults.append(Adddate)
                    # Remit To zip
                    Tozip = listitem[11]
                    Tozip = self.SAS(Tozip)
                    SearchResults.append(Tozip)
                    # Remit To state
                    Tostate = listitem[12]
                    Tostate = self.SAS(Tostate)
                    SearchResults.append(Tostate)
                    # Remit to City
                    Tocity = listitem[13]
                    Tocity = self.SAS(Tocity)
                    SearchResults.append(Tocity)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_POADDR01:
            print (Error_POADDR01)
            return 2        
            
    def Purchase_Order_Current_Comments(self, purno):
        '''
        Searches the current fiscal period for Accpac Purchase Order Comments pertaining to the order
        ------
        Searches Table Pocomm01
        '''
        try:
            purno = self.SAS(purno)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Purno, Comment, Adduser, Adddate  from pocomm01 WHERE TRIM(pocomm01.Purno) LIKE "     '''+purno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Purchase Number
                    Purno = listitem[0]
                    Purno = self.SAS(Purno)
                    SearchResults.append(Purno)
                    # Comment
                    Comment = listitem[1]
                    Comment = self.SAS(Comment)
                    SearchResults.append(Comment)
                    # Added by user
                    Adduser = listitem[2]
                    Adduser = self.SAS(Adduser)
                    SearchResults.append(Adduser)
                    # Added on Date
                    Adddate = listitem[3]
                    Adddate = self.SAS(Adddate)
                    SearchResults.append(Adddate)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_POCOMM01:
            print (Error_POCOMM01)
            return 2
        
    def Accounts_Receivable_Current_Header(self, invno):
        '''
        Searches the current fiscal period for Accpac invoice headers
        ------
        Searches Table Armast01
        '''
        try:
            invno = "%"+self.SAS(invno) +"%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Invno, Custno, Artype, Arstat, Ornum, Ponum, Sotrack, Storenr, Invamt, Paidamt, Balance from armast01 WHERE TRIM(armast01.Invno) LIKE "'''+invno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Invoice Number
                    Invno = self.SAS(listitem[0])
                    SearchResults.append(Invno)
                    # Custno
                    Custno = self.SAS(listitem[1])
                    SearchResults.append(Custno)
                    # Invoice Type
                    Artype = self.SAS(listitem[2])
                    SearchResults.append(Artype)
                    # Invoice Status
                    Arstat = self.SAS(listitem[3])
                    SearchResults.append(Arstat)
                    # Order Number
                    Ornum = self.SAS(listitem[4])
                    SearchResults.append(Ornum)
                    # Purchase Order Number
                    Ponum = self.SAS(listitem[5])
                    SearchResults.append(Ponum)
                    # Sales Order tracking number
                    Sotrack = self.SAS(listitem[6])
                    SearchResults.append(Sotrack)
                    # Store Number
                    Storenr = self.SAS(listitem[7])
                    SearchResults.append(Storenr)
                    # Invoice amount
                    Invamt = self.SAS(listitem[8])
                    SearchResults.append(Invamt)
                    # Paid Amount
                    Paidamt = self.SAS(listitem[9])
                    SearchResults.append(Paidamt)
                    # Balance
                    Balance = self.SAS(listitem[10])
                    SearchResults.append(Balance)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_ARMAST01:
            print (Error_ARMAST01)
            return 2
    def Accounts_Receivable_Current_Items(self, invno):
        '''
        Searches the current fiscal period for Accpac invoices line items
        ------
        Searches Table Artran01
        '''
        try:
            invno = "%"+self.SAS(invno) +"%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Invno, Ponum, Item, Descrip, Custno,Loctid,Serial,Cost,Price,Qtyord,Qtyshp,Extprice, Artype, Adduser from artran01 WHERE TRIM(artran01.Invno) LIKE "'''+invno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Invoice Number
                    Invno = self.SAS(listitem[0])
                    SearchResults.append(Invno)
                    # Purchase Order Number
                    Ponum = self.SAS(listitem[1])
                    SearchResults.append(Ponum)
                    # Item
                    Item = self.SAS(listitem[2])
                    SearchResults.append(Item)
                    # Description
                    Descrip = self.SAS(listitem[3])
                    SearchResults.append(Descrip)
                    # Customer Location Number
                    Custno = self.SAS(listitem[4])
                    SearchResults.append(Custno)
                    # Location code
                    Loctid = self.SAS(listitem[5])
                    SearchResults.append(Loctid)
                    # Item serial Number
                    Serial = self.SAS(listitem[6])
                    SearchResults.append(Serial)
                    # Unit Item Cost
                    Cost = self.SAS(listitem[7])
                    SearchResults.append(Cost)
                    # Unit Item Price
                    Price = self.SAS(listitem[8])
                    SearchResults.append(Price)
                    # Quantity Ordered
                    Qtyord = self.SAS(listitem[9])
                    SearchResults.append(Qtyord)
                    # Quantity Shipped
                    Qtyshp = self.SAS(listitem[10])
                    SearchResults.append(Qtyshp)
                    # Extended Item Price
                    Extprice = self.SAS(listitem[11])
                    SearchResults.append(Extprice)
                    # Invoice types
                    Artype = self.SAS(listitem[12])
                    SearchResults.append(Artype)
                    # Invoice Add user
                    Adduser = self.SAS(listitem[13])
                    SearchResults.append(Adduser)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_ARTRAN01:
            print (Error_ARTRAN01)
            return 2    
    def Accounts_Payable_Current_Header(self, invno):
        '''
        Searches the current fiscal period for Accpac payable header
        ------
        Searches Table Apmast01
        '''
        try:
            invno = "%"+self.SAS(invno) +"%"
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT Invno, Vendno, Pterms, Purdate, Duedate,Puramt,Paidamt,Ref,Checkno,Chkacc,Adduser from apmast01 WHERE TRIM(apmast01.Invno) LIKE "'''+invno+'''" '''
            c.execute(SQL)
            rows = c.fetchall()# or c.fetchall for all the results
            c.close()
            RowsOfResults = []
            if rows:
                for listitem in rows:
                    SearchResults = []
                    # Invoice Number
                    Invno = self.SAS(listitem[0])
                    SearchResults.append(Invno)
                    # Vendor Code
                    Vendno = self.SAS(listitem[1])
                    SearchResults.append(Vendno)
                    # Pay terms
                    Pterms = self.SAS(listitem[2])
                    SearchResults.append(Pterms)
                    # Purchase Date
                    Purdate = self.SAS(listitem[3])
                    SearchResults.append(Purdate)
                    # Due Date
                    Duedate = self.SAS(listitem[4])
                    SearchResults.append(Duedate)
                    # Purchase Amount Cash
                    Puramt = self.SAS(listitem[5])
                    SearchResults.append(Puramt)
                    # Purchase cash paid to date
                    Paidamt = self.SAS(listitem[6])
                    SearchResults.append(Paidamt)
                    # Reference field
                    Ref = self.SAS(listitem[7])
                    SearchResults.append(Ref)
                    # Check Number
                    Checkno = self.SAS(listitem[8])
                    SearchResults.append(Checkno)
                    # Check Account Number
                    Chkacc = self.SAS(listitem[9])
                    SearchResults.append(Chkacc)
                    # Adduser
                    Adduser = self.SAS(listitem[10])
                    SearchResults.append(Adduser)
                    #
                    RowsOfResults.append(SearchResults)
                return RowsOfResults
            else:
                print("No row: value - %s"% (str(rows)))
                return 1
        except Exception as Error_APMAST01:
            print (Error_APMAST01)
            return 2    
        
#NP = Accpac()
#Result = NP.Accounts_Payable_Current_Header('PO75299')
#print (Result)