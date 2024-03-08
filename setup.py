from setuptools import find_packages, setup
from typing import List

def get_requirements(path_to_requirements_dot_txt: str)->List[str]:
    '''
    This function imports each library name mentioned in each line of the requirements.txt file
    '''
    to_import = []
    with open(path_to_requirements_dot_txt) as file_obj: 
        to_import = file_obj.readlines() #works like split() puts each item in list
    to_import = [each_item.replace("\n", "") for each_item in to_import] # to get rid of the \n for new line
    
    hyphen_e_space_dot = '-e .'
    if hyphen_e_space_dot in to_import: 
        to_import.remove(hyphen_e_space_dot)
    #function get_requirements ends here



# this setup.py file builds the packages. 
# to trigger this from requirements.txt we 
#       add a "-e ." at the last line of the requirements.txt file. 


setup(
name='mlproject', 
version='0.0.1', 
author='Dwai', 
author_email='dwaipayansamaddar0607@gmail.com', 
packages=find_packages(), 
install_requires=get_requirements('requirements.txt')                   #['pandas', 'numpy', 'matplotlib', 'seaborn']
)
