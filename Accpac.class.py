import pyodbc

class Accpac:
    '''
    Handles Accpac Queries.
    Make sure there is an ODBC with ODBC-32 installed.
    '''

    def Open_Sales_Order_Search(self, item):
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT custno, sono, qtyord, qtyshp, rqdate from Sotran01 WHERE TRIM(sotran01.item) LIKE "'''+item+'''" AND sostat = '' '''
            c.execute(SQL)
            row = c.fetchall()# or c.fetchall for all the results
            c.close()
            if row:
                for listitem in row:
                    custno = listitem[0]
                    sono = listitem[1]
                    qtyord = listitem[2]
                    qtyshp = listitem[3]
                    rqdate = listitem[4]
                    print (rqdate)
            else:
                print("No row: value - %s"% (str(row)))
        except Exception as E:
            print (E)
            
            
    def History_Sales_Order_Search(self, item):
        try:
            item=str(item)
            cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
            c = cnxn.cursor()
            SQL = '''SELECT custno, sono, qtyord, qtyshp, shipdate, Sostat, Sotype, Serial from Soytrn01 WHERE TRIM(soytrn01.item) LIKE "'''+item+'''" '''
            c.execute(SQL)
            row = c.fetchall()# or c.fetchall for all the results
            c.close()
            SearchResults = []
            if row:
                for listitem in row:
                    custno = listitem[0]
                    SearchResults.append(custno)
                    #
                    sono = listitem[1]
                    SearchResults.append(sono)
                    #
                    qtyord = listitem[2]
                    SearchResults.append(qtyord)
                    #
                    qtyshp = listitem[3]
                    SearchResults.append(qtyship)
                    #
                    rqdate = listitem[4]
                    SearchResults.append(rqdate)
                    #
                    return SearchResults
            else:
                print("No row: value - %s"% (str(row)))
                return 1
        except Exception as Error_SO_History:
            print (Error_SO_History)
            return 2
            
            
            
            
AP = Accpac()
AP.Open_Sales_Order_Search(item="TEST")