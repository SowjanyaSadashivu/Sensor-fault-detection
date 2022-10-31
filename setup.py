import imp
from typing import List
from urllib import request
from setuptools import find_packages,setup 
from typing import List
# hover on find_packages: return list(packages or modules) of python items.

#to get the requirements from requirements and pass it as list to install_requires.
def get_requirements( )->List[str]:
    """
    this function will return list of requirements.

    """
    requirements_list:List[str]= []


    """
    write a code to rad requirements.txt file and append each requirements in requirements_list variable.
    """
    return requirements_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Sowjanya",
    author_email= "sadashivusowjanya@gmail.com",
    packages=find_packages(), 
    install_requires =get_requirements(),
) 