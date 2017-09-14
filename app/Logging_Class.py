# #############
# @Title: Logging Class
# @Purpose: easy access functions to log with
# @Author: Patrick Hastings
# @Notes: Best use is logging and printing
#
# ############
#

import logging, sys, time, os, platform, getpass, socket


class Logger:
    '''
    Logging class, optimized for windows.
    Pass it a programname and version for parameters upon first initialization.
    '''
    def __init__(self, programname='Default Program', version= '1'):
        '''
        Initializes required variables
        '''
        try:
            logdate = time.strftime('Date %m-%d-%y'+' Time-%H-%M')
            program = programname
            str(logdate)
            machname = platform.node()
            machhost = socket.gethostname()
            user = os.path.join(os.path.expandvars("%userprofile%"),"Documents and Settings")
            logging.basicConfig(format='%(asctime)s %(message)s',level=logging.INFO, filename=program + logdate + '.log')
            logging.info('Starting Program: Version '+version)
            logging.info('Program running on network host:' + machhost + ' with a local machine name of:' + machname)
            logging.info('The user running this program is: '+ user)
        except Exception as Eval4:
            Eval4 = str(Eval4)
            print('Error 4: Logging module: Error while initializing Logger: '+ Eval4)
            
            
    def lap(self, *args):
        '''
        Log and print at the same time.
        Includes and uses time mod and log mod
        uses *args to take multiple parameters
        '''
        try:
            for item in enumerate(args):
                logging.info(time.ctime()+" :  "+str(args))
                print(time.ctime() +":   "+str(args))
        except Exception as Eval5:
            print('Ran into Error 5 while trying to log and print in the Logging Class Module: '+str(Eval5))