## this is responsible to create my ML application as a package , and can use it 

from setuptools import find_packages , setup
from typing import List
  
HYPEN_E_DOR = '-e .'  
def get_requirements(file_path:str)->List[str]:
    ## this function will return list of requirements 
    requirements = [] 
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements ]

        if HYPEN_E_DOR in requirements:
            requirements.remove(HYPEN_E_DOR)
            
    return requirements        
setup(
    name = 'ML',
    version='0.0.1',
    author='Raja',
    author_email='raja.sodani@gmai;.com',
    packages=find_packages(),
    ##install_requires = ['pandas','numpy','seaborn']  
    install_requires = get_requirements('requirement.txt')  
    
) 