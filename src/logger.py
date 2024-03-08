# needed for loggin in
import logging
import os
from datetime import datetime

my_log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #setting up format for my log file naming convention
logs_path=os.path.join(os.getcwd(),"logs_", my_log_file) #setting up full file path
os.makedirs(logs_path, exist_ok=True) #even if there's a folder, and there's a file.. keep on appending files.

path_my_log_file = os.path.join(logs_path, my_log_file)

logging.basicConfig(
    filename=path_my_log_file, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)

# below code was used for testing
# if __name__=="__main__":
#     logging.info("logging has started!")