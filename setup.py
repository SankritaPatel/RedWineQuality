from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '')for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='RedWineQuality',
    version='0.0.1',
    author='SankritaPatel',
    author_email='sankrita6960@outlook.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
    description="A Ml Project that predict Red Wine Quality",
    url="https://github.com/SankritaPatel/RedWineQuality"
)