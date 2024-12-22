from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This func weill return list of requirements
    :param file_path:
    :return:
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', '') for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='mlporoject',
    version='0.0.1',
    author='sunny sogani',
    author_email='sunnysogani@gmail.com',
    install_requires=get_requirements('requirements.txt')

)