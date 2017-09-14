# ##################
# @Author: Patrick Hastings
# @Date: 8-17-2017
# @Title: Accpac_class unit testing
# @Purpose: Times each function run, and gets the time per function run
# ##################
import accpac_class
import unittest
import time

class AccpacTest(unittest.TestCase):
    '''
    Tests Acccpac class code
    '''
    SLOW_TEST_THRESHOLD = 0.3
    
    def setUp(self):
        '''
        Hooks to unit test to make calls to the timer
        '''
        self._started_at = time.time()
    
    def tearDown(self):
        '''
        Hooks to unit test to get the module and time for each function
        '''
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))
        # SLOW_TEST_THRESHOLD = 0.3
        # Commented out only print slow test threshold
        #if elapsed > SLOW_TEST_THRESHOLD:
            #print('{} ({}s)'.format(self.id(), round(elapsed, 2)))        
    def test_AR_Header_Current(self):
        '''
        Tests the current fiscal period of accounts receivable header search function
        Accpac table Armast01
        '''
        AP = accpac_class.Accpac()
        Teststring = '188942'
        Result = AP.Accounts_Receivable_Current_Header(invno=Teststring)
        self.assertEqual(Result[0][0],'188942')
        self.assertEqual(Result[0][1], 'SUPERG')
        self.assertEqual(Result[0][2],'C')
        self.assertEqual(Result[0][3],'')
        self.assertEqual(Result[0][4],'177154')
        self.assertEqual(Result[0][5],'Attn martha')
        self.assertEqual(Result[0][6], 'RMA#E176502')
        self.assertEqual(Result[0][7], '')
        self.assertEqual(Result[0][8], '-516')
        self.assertEqual(Result[0][9], '-93.8')
        self.assertEqual(Result[0][10], '-422.2')
        del AP    

    def test_AR_Items_Current(self):
        '''
        Tests the current fiscal period of accounts receivable items search function
        Accpac table Artran01
        '''
        AP = accpac_class.Accpac()
        Teststring = '188942'
        Result = AP.Accounts_Receivable_Current_Items(invno=Teststring)
        self.assertEqual(Result[0][0],'188942')
        self.assertEqual(Result[0][1], 'Our SO # 177154')
        self.assertEqual(Result[0][2],'4610-TI9')
        self.assertEqual(Result[0][3],'Printer, SureMark Thermal Receipt')
        self.assertEqual(Result[0][4],'SUPERG')
        self.assertEqual(Result[0][5],'RMAWIP')
        self.assertEqual(Result[0][6], '82')
        self.assertEqual(Result[0][7], '0')
        self.assertEqual(Result[0][8], '129')
        self.assertEqual(Result[0][9], '-4')
        self.assertEqual(Result[0][10], '-4')
        self.assertEqual(Result[0][11], '-516')
        self.assertEqual(Result[0][12], 'C')
        self.assertEqual(Result[0][13], 'RM')
        del AP    
        
    def test_AP_Header_Current(self):
        '''
        Tests the search function to find invoices in accounts payable in current fiscal period
        Accpac table Apmast01
        '''
        AP = accpac_class.Accpac()
        Teststring = 'PO75299'
        Result = AP.Accounts_Payable_Current_Header(invno=Teststring)
        self.assertEqual(Result[0][0],'PO75299')
        self.assertEqual(Result[0][1], 'TMCOMP')
        self.assertEqual(Result[0][2],'')
        self.assertEqual(Result[0][3],'2009-06-15')
        self.assertEqual(Result[0][4],'2009-06-15')
        self.assertEqual(Result[0][5],'-31300')
        self.assertEqual(Result[0][6], '0')
        self.assertEqual(Result[0][7], 'PREPAY')
        self.assertEqual(Result[0][8], '25752')
        self.assertEqual(Result[0][9], '1002-000')
        self.assertEqual(Result[0][10], 'AH')
        del AP    
        
        
    def test_Open_SO_Search(self):
        '''
        Tests the Open Sales order search tool
        '''
        AP = accpac_class.Accpac()
        Result = AP.Open_Sales_Order_Search(item="TEST")        
        self.assertEqual(Result[0][0],'HSG')
    
    def test_Hist_SO_Search(self):
        '''
        Tests the sales order history search tool
        '''
        AP = accpac_class.Accpac()
        Result = AP.Sales_History_Order_Search(item="TEST")
        self.assertEqual(Result[0][0], 'NUKE')
        self.assertEqual(Result[0][1], '240907')
        self.assertEqual(Result[0][2], '0')
        self.assertEqual(Result[0][3], '1')
        self.assertEqual(Result[0][4], '2014-10-06')
        
    def test_Open_PO_Search(self):
        '''
        Tests the sales orders that searches this fiscal period
        '''
        AP = accpac_class.Accpac()
        Teststring = "TEST"
        Result = AP.Purchase_Search(item=Teststring)
        self.assertEqual(Result[0][0], '175632')
        self.assertEqual(Result[0][1], '03820')
        self.assertEqual(Result[0][2], '0')
        self.assertEqual(Result[0][3], '3')
        self.assertEqual(Result[0][4], '0')
        self.assertEqual(Result[0][5], '')
        
    def test_Hist_PO_Search(self):
        '''
        Tests the History Purchase order search tool
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Purchase_History_Search(item=Teststring)
        self.assertEqual(Result[0][0], '156524')
        self.assertEqual(Result[0][1], 'CPW')
        self.assertEqual(Result[0][2], '0')
        self.assertEqual(Result[0][3], '1')
        self.assertEqual(Result[0][4], '1')
        self.assertEqual(Result[0][5], 'C')
    
    def test_SAS(self):
        '''
        Tests the strip and string.
        Feeds in a unicode string with spaces
        Expects back a regular string
        '''
        AP = accpac_class.Accpac()
        TestString = 'bob  '
        TestString = TestString.encode('utf-8')
        TheReturnedString = AP.SAS(Obj=TestString)
        self.assertEqual(TheReturnedString, 'bob')
        del AP
    
    def test_Item_Search(self):
        '''
        Tests the QTY item search for current period
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Search(item=Teststring)
        self.assertEqual(Result[0][0],'TEST')
        self.assertEqual(Result[0][1], 'FG')
        self.assertEqual(Result[0][2],'2')
        self.assertEqual(Result[0][3],'0')
        self.assertEqual(Result[0][4],'TBT')
        self.assertEqual(Result[0][5],'TBT')
        self.assertEqual(Result[0][6], '15')
        del AP
    def test_Item_By_Location_Search(self):
        '''
        Tests the QTY item search for current period by search location
        '''
        AP = accpac_class.Accpac()
        Teststring = 'FG'
        Result = AP.Items_by_Location_Search(loctid=Teststring)
        self.assertEqual(Result[0][0],'CITIBANK3036')
        self.assertEqual(Result[0][1], 'FG')
        self.assertEqual(Result[0][2],'19')
        self.assertEqual(Result[0][3],'0')
        self.assertEqual(Result[0][4],'')
        self.assertEqual(Result[0][5],'')
        self.assertEqual(Result[0][6], '1')
        del AP    
    def test_Item_Header_Search(self):
        '''
        Tests the Item Master ledger/header info search
        Icitem
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Header_Search(item=Teststring)
        self.assertEqual(Result[0][0],'TEST')
        self.assertEqual(Result[0][1], 'Test P/N')
        self.assertEqual(Result[0][2],'')
        self.assertEqual(Result[0][3],'')
        self.assertEqual(Result[0][4],'')
        self.assertEqual(Result[0][5],'')
        self.assertEqual(Result[0][6], 'TEST60')
        self.assertEqual(Result[0][7], 'TEST70')
        self.assertEqual(Result[0][8], '')
        self.assertEqual(Result[0][9], '')
        self.assertEqual(Result[0][10], '')
        self.assertEqual(Result[0][11], '4')
        self.assertEqual(Result[0][12], '2017-04-11')
        self.assertEqual(Result[0][13], '2017-08-08')
        self.assertEqual(Result[0][14], '1899-12-30')
        self.assertEqual(Result[0][15], '2017-08-17')
        self.assertEqual(Result[0][16], '0')
        del AP    
        
    def test_Item_Cost_Search(self):
        '''
        Tests the item cost tier search for current period
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Cost_Search(item=Teststring)
        self.assertEqual(Result[0][0], 'TEST')
        self.assertEqual(Result[0][1],'FG')
        self.assertEqual(Result[0][2], '1075077')
        self.assertEqual(Result[0][3],'0')
        self.assertEqual(Result[0][4],'0')
        self.assertEqual(Result[0][5],'KW')
        del AP
    def test_Item_Transaction_Search(self):
        '''
        Tests the item transaction history search for current fiscal period
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Transaction_Search(item=Teststring)
        self.assertEqual(Result[0][0], '4287875')
        self.assertEqual(Result[0][1], '16')
        self.assertEqual(Result[0][2], 'FG')
        self.assertEqual(Result[0][3], 'TEST')
        self.assertEqual(Result[0][4], '1108452')
        self.assertEqual(Result[0][5], '')
        self.assertEqual(Result[0][6], 'R')
        self.assertEqual(Result[0][7], '')
        self.assertEqual(Result[0][8], '1')
        self.assertEqual(Result[0][9], '0')
        self.assertEqual(Result[0][10], '')
        self.assertEqual(Result[0][11], '769248')
        self.assertEqual(Result[0][12], 'DAMIONS')
    def test_Item_Transaction_History_Search(self):
        '''
        Tests the item transaction history search for current fiscal period
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Transaction_History_Search(item=Teststring)
        self.assertEqual(Result[0][0], '2717654')
        self.assertEqual(Result[0][1], '2')
        self.assertEqual(Result[0][2], 'FG')
        self.assertEqual(Result[0][3], 'TEST')
        self.assertEqual(Result[0][4], '336743')
        self.assertEqual(Result[0][5], 'Shipment SO#    240907')
        self.assertEqual(Result[0][6], 'I')
        self.assertEqual(Result[0][7], '2014-10-06')
        self.assertEqual(Result[0][8], '')
        self.assertEqual(Result[0][9], '-1')
        self.assertEqual(Result[0][10], '0')
        self.assertEqual(Result[0][11], '0')
        self.assertEqual(Result[0][12], 'NUKE')
        self.assertEqual(Result[0][13], '240907')
        self.assertEqual(Result[0][14], 'AMY')
        self.assertEqual(Result[0][15], 'TURCHINETZ')
    def test_Item_Location_Search(self):
        '''
        Tests the items at location search function for current fiscal period
        Iciloc
        '''
        AP = accpac_class.Accpac()
        Teststring = 'TEST'
        Result = AP.Item_Location_Search(item=Teststring)
        self.assertEqual(Result[0][0], 'TEST')
        self.assertEqual(Result[0][1], 'WIP')
        self.assertEqual(Result[0][2], '0')
        self.assertEqual(Result[0][3], '0')
        self.assertEqual(Result[0][4], '0')
        self.assertEqual(Result[0][5], '0')
        self.assertEqual(str(Result[0][6]), '1899-12-30')
        self.assertEqual(str(Result[0][7]), '1899-12-30')
        

    def test_Sales_Header_Current(self):
        '''
        Tests the Sales order header search
        '''
        AP = accpac_class.Accpac()
        Teststring = '41877'
        Result = AP.Sales_Order_Header_Current_Search(sono=Teststring)
        self.assertEqual(Result[0][0], '41877')
        self.assertEqual(Result[0][1], 'PCMALL')
        self.assertEqual(str(Result[0][2]), '2004-04-09')
        self.assertEqual(str(Result[0][3]), '2004-09-22')
        self.assertEqual(Result[0][4], 'FEDP')
        self.assertEqual(Result[0][5], '90010')
        self.assertEqual(Result[0][6], 'Net 30 Days')
        self.assertEqual(Result[0][7], '0')
        self.assertEqual(Result[0][8], '0')
    def test_Sales_Comment_Search(self):
        '''
        Tests the sales order comment search function
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring = '41877'
            Result = AP.Sales_Order_Comment_Current_Search(sono=Teststring)
            self.assertEqual(Result[0][0], '41877')
            self.assertEqual(Result[0][1], '')
            self.assertEqual(Result[0][2], 'GY')
            self.assertEqual(str(Result[0][3]), '2010-04-05')
        except Exception as TSCSError:
            TSCSError = str(TSCSError)
            print(TSCSError)
    def test_Sales_Address_Search(self):
        '''
        Tests Accpac's ability to search for sales orders in current fiscal period
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='41877'
            Result = AP.Sales_Order_Address_Current_Search(sono=Teststring)
            self.assertEqual(Result[0][0], 'PCPC')
            self.assertEqual(Result[0][1], '41877')
            self.assertEqual(Result[0][2], 'California Family Health Council')
            self.assertEqual(Result[0][3], '3600 Wilshire Blvd. Suite 600')
            self.assertEqual(Result[0][4], '')
            self.assertEqual(Result[0][5], '')
            self.assertEqual(Result[0][6], 'Los Angeles')
            self.assertEqual(Result[0][7], 'CA')
            self.assertEqual(Result[0][8], '90010')
            self.assertEqual(Result[0][9], '90010')
            self.assertEqual(Result[0][10], 'JMH')
            self.assertEqual(str(Result[0][11]), '2014-09-16')
        except Exception as TSASError:
            TSASError = str(TSASError)
            print (TSASError)
    def test_Sales_Item_Search(self):
        '''
        Tests Accpac's ability to search for sales orders in current fiscal period
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='41877'
            Result = AP.Sales_Order_Item_Current_Search(sono=Teststring)
            self.assertEqual(Result[0][0], '41877')
            self.assertEqual(Result[0][1], 'PCMALL')
            self.assertEqual(Result[0][2], 'C4110-67923')
            self.assertEqual(Result[0][3], 'Kit, Maintenance')
            self.assertEqual(Result[0][4], '0')
            self.assertEqual(Result[0][5], '365')
            self.assertEqual(Result[0][6], '2004-09-22')
            self.assertEqual(Result[0][7], '0')
            self.assertEqual(Result[0][8], '1')
            self.assertEqual(Result[0][9], '0')
            self.assertEqual(Result[0][10], '365')
            self.assertEqual(Result[0][11], '0')
        except Exception as TSISError:
            TSISError = str(TSISError)
            print (TSISError)
    def test_Sales_Header_History_Search(self):
        '''
        Tests Accpac's ability to search for header entry records in the historical period.
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='155510'
            Result = AP.Sales_Order_Header_History_Search(sono=Teststring)
            self.assertEqual(Result[0][0], '155510')
            self.assertEqual(Result[0][1], 'YCREP')
            self.assertEqual(Result[0][2], '196055')
            self.assertEqual(Result[0][3], 'C')
            self.assertEqual(Result[0][4], '0')
            self.assertEqual(Result[0][5], '79')
            self.assertEqual(Result[0][6], '2012-01-01')
            self.assertEqual(Result[0][7], '2012-01-01')
            self.assertEqual(Result[0][8], '')
            self.assertEqual(Result[0][9], '')
        except Exception as SOHErrorTest:
            print(SOHErrorTest)
        
    def test_Sales_Address_History_Search(self):
        '''
        Tests Accpac's ability to search for sales orders in historical fiscal records
        Table: soyadr
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='155510'
            Result = AP.Sales_Order_Address_History_Search(sono=Teststring)
            self.assertEqual(Result[0][0], 'YCREP')
            self.assertEqual(Result[0][1], '155510')
            self.assertEqual(Result[0][2], 'Yankee Candle Company')
            self.assertEqual(Result[0][3], 'The Crossing @ Smithfield')
            self.assertEqual(Result[0][4], '371 Putnam Pke Suite 550')
            self.assertEqual(Result[0][5], '')
            self.assertEqual(Result[0][6], 'Smithfield')
            self.assertEqual(Result[0][7], 'RI')
            self.assertEqual(Result[0][8], '02917')
            self.assertEqual(Result[0][9], '211')
            self.assertEqual(Result[0][10], 'SC')
            self.assertEqual(str(Result[0][11]), '2012-01-02')
        except Exception as TSASError:
            TSAHSError = str(TSAHSError)
            print (TSAHSError)    
    def test_Purchase_Order_Current_Search(self):
        '''
        Tests Accpac's ability to search for sales orders in current fiscal period
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='29727'
            Result = AP.Purchase_Order_Current_Search(purno=Teststring)
            self.assertEqual(Result[0][0], '29727')
            self.assertEqual(Result[0][1], 'GECAPT')
            self.assertEqual(Result[0][2], 'GE Capital Corporation')
            self.assertEqual(Result[0][3], '-1120')
            self.assertEqual(Result[0][4], '2005-10-03')
            self.assertEqual(Result[0][5], '0')
            self.assertEqual(Result[0][6], '2005-10-03')
            self.assertEqual(Result[0][7], 'FG')
            self.assertEqual(Result[0][8], 'UPS')
            self.assertEqual(Result[0][9], '')
            self.assertEqual(Result[0][10], 'R')
            self.assertEqual(Result[0][11], '')
            self.assertEqual(Result[0][12], 'AH')
            self.assertEqual(Result[0][13], '2005-10-03')
        except Exception as TPOCSError:
            TPOCSError = str(TPOCSError)
            print (TPOCSError)
    def test_Purchase_Order_Current_Items_Search(self):
        '''
        Tests Accpac's ability to search for line items
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='29727'
            Result = AP.Purchase_Order_Current_Items(purno=Teststring)
            self.assertEqual(Result[0][0], '29727')
            self.assertEqual(Result[0][1], '5060-002')
            self.assertEqual(Result[0][2], 'Printer, C750N, Lexmark')
            self.assertEqual(Result[0][3], '280')
            self.assertEqual(Result[0][4], '-4')
            self.assertEqual(Result[0][5], '0')
            self.assertEqual(Result[0][6], '2005-10-03')
            self.assertEqual(Result[0][7], '-1120')
            self.assertEqual(Result[0][8], '1899-12-30')
            self.assertEqual(Result[0][9], '2005-10-03')
            self.assertEqual(Result[0][10], '1140-000')
            self.assertEqual(Result[0][11], 'FG')
            self.assertEqual(Result[0][12], '')
            self.assertEqual(Result[0][13], 'R')
            self.assertEqual(Result[0][14], '1')
        except Exception as TPOCISError:
            TPOCISError = str(TPOCISError)
            print (TPOCISError)
    def test_Purchase_Order_Current_Address_Search(self):
        '''
        Tests Accpac's ability to search for A Purchase Orders address details
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='77901'
            Result = AP.Purchase_Order_Current_Address(purno=Teststring)
            self.assertEqual(Result[0][0], '77901')
            self.assertEqual(Result[0][1], 'Radiant Systems, Inc')
            self.assertEqual(Result[0][2], '6610 Shiloh Rd. East')
            self.assertEqual(Result[0][3], '')
            self.assertEqual(Result[0][4], '')
            self.assertEqual(Result[0][5], 'Radiant Systems Unfinished Goods-No')
            self.assertEqual(Result[0][6], '')
            self.assertEqual(Result[0][7], '')
            self.assertEqual(Result[0][8], '')
            self.assertEqual(Result[0][9], 'SC')
            self.assertEqual(Result[0][10], '2009-10-12')
            self.assertEqual(Result[0][11], '30005')
            self.assertEqual(Result[0][12], 'GA')
            self.assertEqual(Result[0][13], 'Alpharetta')
        except Exception as TPOCASError:
            TPOCASError = str(TPOCASError)
            print (TPOCASError)
            
    def test_Purchase_Order_Current_Comments_Search(self):
        '''
        Tests Accpac's ability to search for A Purchase Orders address details
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='29727'
            Result = AP.Purchase_Order_Current_Comments(purno=Teststring)
            self.assertEqual(Result[0][0], '29727')
            self.assertEqual(Result[0][1], 'MC   5569 2850 0001 5429     11/12 Scott Johnson (858)')
            self.assertEqual(Result[0][2], 'AH')
            self.assertEqual(Result[0][3], '2005-10-03')
        except Exception as TPOCCSError:
            TPOCCSError = str(TPOCCSError)
            print (TPOCCSError)
    
    def test_Purchase_Order_Historical_Items_Search(self):
        '''
        Tests Accpac's ability to search for line items
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='96841'
            Result = AP.Purchase_Order_History_Items(purno=Teststring)
            self.assertEqual(Result[0][0], '96841')
            self.assertEqual(Result[0][1], '40Y9033')
            self.assertEqual(Result[0][2], 'Hard Drive, 40GB 7200RPM, SATA')
            self.assertEqual(Result[0][3], '0')
            self.assertEqual(Result[0][4], '1')
            self.assertEqual(Result[0][5], '0')
            self.assertEqual(Result[0][6], '2012-01-01')
            self.assertEqual(Result[0][7], '0')
            self.assertEqual(Result[0][8], '2012-01-01')
            self.assertEqual(Result[0][9], '2012-01-01')
            self.assertEqual(Result[0][10], '1140-000')
            self.assertEqual(Result[0][11], 'YC-UFG')
            self.assertEqual(Result[0][12], 'X')
            self.assertEqual(Result[0][13], '')
            self.assertEqual(Result[0][14], '1')
        except Exception as TPOHIError:
            TPOHIError = str(TPOHIError)
            print (TPOHIError)    
    
    def test_Summary_Item_Search(self):
        '''
        Tests Accpac's ability to search run general item summary searches
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='TESTEZ'
            Result = AP.Summary_Item_Search(item=Teststring)
            self.assertEqual(Result[0][0], 'TESTEZ')
            self.assertEqual(Result[0][1], 'Test EZ Drive')
            self.assertEqual(Result[0][2], '0')
            self.assertEqual(Result[0][3], '0')
            self.assertEqual(Result[0][4], '')
            self.assertEqual(Result[0][5], '1899-12-30')
            self.assertEqual(Result[0][6], '1899-12-30')
            self.assertEqual(Result[0][7], '1998-02-03')
        except Exception as TSISError:
            TSISError = str(TSISError)
            print (TSISError)
    def test_Summary_Sales_Order_Search(self):
        '''
        Tests Accpac's ability to search run general sales order summary searches
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='155510'
            Result = AP.Summary_Sales_Order_Search(sono=Teststring)
            self.assertEqual(Result[0][0], '155510')
            self.assertEqual(Result[0][1], 'C')
            self.assertEqual(Result[0][2], '196055')
            self.assertEqual(Result[0][3], 'YCREP')
            self.assertEqual(Result[0][4], '211')
            self.assertEqual(Result[0][5], '2012-01-01')
            self.assertEqual(Result[0][6], '2012-01-01')
            self.assertEqual(Result[0][7], '')
            self.assertEqual(Result[0][8], '')
        except Exception as TSSOSError:
            TSSOSError = str(TSSOSError)
            print (''+str(TSSOSError))    
    def test_Summary_Purchase_Order_Search(self):
        '''
        Tests Accpac's ability to search run general purchase order summary searches
        '''
        try:
            AP = accpac_class.Accpac()
            Teststring='418'
            Result = AP.Summary_Sales_Order_Search(sono=Teststring)
            self.assertEqual(Result[0][0], '41877')
            self.assertEqual(Result[0][1], '')
            self.assertEqual(Result[0][2], '354285')
            self.assertEqual(Result[0][3], 'PCMALL')
            self.assertEqual(Result[0][4], '90010')
            self.assertEqual(Result[0][5], '2004-04-09')
            self.assertEqual(Result[0][6], '2004-09-22')
            self.assertEqual(Result[0][7], 'O')
            self.assertEqual(Result[0][8], '647002847740')
        except Exception as TSPOSError:
            TSPOSError = str(TSPOSError)
            print (''+str(TSPOSError))        
# Run Silos
if __name__ == '__main__':
    unittest.main()