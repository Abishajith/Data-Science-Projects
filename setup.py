from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []  #make requirement.txt as list

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(
    name="cost",
    version="0.0.1",
    author="abi",
    author_email="abisha2306@gmail.com",
    packages = find_packages(),   ##equalent to -e.
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)
