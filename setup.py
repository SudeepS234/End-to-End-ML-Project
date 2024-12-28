from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #readlines() method will read \n also from the requirements file so this list comprehension is done to replace it with blank 
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='E2E-MLProject',
    version='0.0.1', 
    author='Sudeep',
    author_email='deepusudeep18@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)