import pyodbc
import datetime
import unittest



class accpac():
    
    def __init__(self):
        '''
        ------
        Properties:\n
        - CurrentDate: Current date of program at runtime
        - SelectedDate: string, full mm/dd/yy
        - SelectedMonth: string, mm, as numeric. for ex January is 01
        - SelectedYear: string, yy, as numeric last two digits of year
        --
        - CFPSalesMade: integer, total number of gross sales made
        
        '''
        self.CurrentDate = ''
        self.CurrentMonth = ''
        self.CurrentYear = ''
        self.CurrentDay = ''
        self.SelectedDate = ''
        self.SelectedMonth = ''
        self.SelectedYear = ''
        #
        # Current Fiscal Period - Sales Orders
        self.CFPSalesMade = 0
        self.CFPSalesLine_total_extprice = 0
        self.CFPSalesLines_total_real = 0
        #
        # Current Fiscal Period - Purchase Orders
        self.CFPPurchasesMade = 0
        self.CFPPurchase_total_extprice = 0
        self.CFPPurchase_total_real = 0
        #
    
    def set_CurrentDate(self):
        '''
        Sets the state of the current date
        ------
        This will set the date variables to the systems date
        '''
        self.CurrentDate = datetime.date.today()
        self.CurrentDay = datetime.datetime.now().strftime("%m")
        self.CurrentMonth = datetime.datetime.now().strftime("%d")
        self.CurrentYear = datetime.datetime.now().strftime("%Y")
        

#TestAccPac = accpac()
#TestAccPac.set_CurrentDate()