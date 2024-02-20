import sys 
from src.logger import logging

def error_message_detail(error,error_detail):
    _,_,exc_tb = error_detail.exc_info()
    ## exc_tb will give infor about which file the exception will occur , and on which line 
    file_name = exc_tb.tb_frame.f_code.co_filename
    ## all the above related values will we found on google with name custom expection
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format (
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
        
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message        
        
        
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")    
        raise CustomException(e,sys)  