from setuptools import find_packages,setup
from typing import List

hyphen_e_dot='-e .'


def get_requirements(file_path:str)->List[str]:
    '''function returns the list of requirements '''
    requirements=[]
    print("first",requirements)
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    print("second",requirements)
    return requirements
    

setup(
    name='students_performance_project',
    version='0.0.1',
    author='sreedevi',
    author_email='sreedevisagar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)