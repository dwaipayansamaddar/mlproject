# needed for exception handling purpose 
# we will use Sys library.. because we can get info about errors from Sys library of Python
import sys
import logging

def my_error_message_detail(error, error_detail: sys): 
    _, _, exc_tbl = error_detail.exc_info() # gives 3 info.. we only care about the third one.. using tuple unpacking
    file_name = exc_tbl.tb_frame.f_code.co_filename
    
    my_error_msg=f"Error occurred in --> script named: [{file_name}]; line number: [{exc_tbl.tb_lineno}]; error message [{str(error)}]"
    return my_error_msg

# we will be inheriting this from the true 'Exception' class
class my_CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = my_error_message_detail(error=error_message, error_detail=error_detail) #using our custom
    def __str__(self): 
        return self.error_message
    
# below code was used for testing
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero error for testing")
#         raise my_CustomException(e, sys)
