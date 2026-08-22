# setup file is essential part of packaging


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this funciton will return list of requirements
    Returns:
        List[str]: _description_
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            # process
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e. (end of file)
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Nicholas TJ",
    author_email="nic@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


