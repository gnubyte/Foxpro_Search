import pyodbc

def appendSOADDR(Custno, Sono, Adtype, Company, address1, address2, address3, City, State, Country, Zip, Cshipno, Adduser, Addtime, Lckstat, Lckuser, Lckdate, Lcktime, Latitude, Longitude, Storenr):
    '''
    Appends Sales Order Address record.
    '''
    try:
        
        cnxn = pyodbc.connect('DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO')
        c = cnxn.cursor()
        querystr = """
        APPEND BLANK REPLACE Custno WITH "%s",
        REPLACE Sono WITH "%s",
        REPLACE Adtype WITH "%s",
        REPLACE Company WITH "%s",
        REPLACE Address1 WITH "%s",
        REPLACE Address2 WITH "%s",
        REPLACE Address3 WITH "%s",
        REPLACE City WITH "%s",
        REPLACE State WITH "%s",
        REPLACE Country WITH "%s",
        REPLACE Zip WITH "%s",
        REPLACE Cshipno WITH "%s",
        REPLACE Adduser WITH "%s",
        REPLACE Addtime WITH "%s",
        REPLACE Lckstat WITH "%s",
        REPLACE Lckuser WITH "%s",
        REPLACE Lckdate WITH "%s",
        REPLACE Lcktime WITH "%s",
        REPLACE Latitude WITH "%s",
        REPLACE Longitude WITH "%s",
        REPLACE Storenr WITH "%s"
        FROM prodata!soaddr01
        
        """ % (Custno, Sono, Adtype, Company, address1, address2, address3, City, State, Country, Zip, Cshipno, Adduser, Addtime, Lckstat, Lckuser, Lckdate, Lcktime, Latitude, Longitude, Storenr )
        c.execute(querystr)
        row = c.fetchall()# or c.fetchall for all the results
        for item in row:
            print(item)
    except Exception as E:
        print ('Exception E-Sales Order Address Line Addition:'+str(E))

appendSOADDR(Custno, Sono, Adtype, Company, address1, address2, address3, 
            City, State, Country, Zip, Cshipno, Adduser, Addtime, 
            Lckstat, Lckuser, Lckdate, Lcktime, Latitude, 
            Longitude, Storenr)



def ReadSOADDR():
    '''
    Reads in Sales Order Address
    '''
    try:
        connection = pyodbc.connect("DRIVER={Microsoft Visual FoxPro-Treiber};SOURCETYPE=DBC;SOURCEDB=P:\PRODATA.DBC;NULL=NO")
        c = connection.cursor()
        c.execute("SELECT Somast01.Sono, Somast01.Custno, Somast01.Sodate, Somast01.Shipvia, Somast01.Cshipno, Somast01.Shpamt, Somast01.Ponum,  Somast01.Salesmn, Somast01.Sostat, Somast01.Sotype, Somast01.Sotrack FROM prodata!somast01")
        c.fetchone()
        if row:
            for item in row:
                print(item)
    except ValueError as Econ30:
        print (str(Econ30))
