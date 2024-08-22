from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
#create a funtion for returning a list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        for line in f:
            requirements.append(line.strip())

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
        
# creating metadata for this ML package
setup(
    name='mlproject',
    version='0.0.1',
    author='bikash',
    author_email='biakshshah565@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)