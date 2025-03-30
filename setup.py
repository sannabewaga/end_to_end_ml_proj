from setuptools import setup, find_packages

from typing import List

const = '-e .'

def get_requirements(file_path:str)-> List[str]:

    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements=   [req.replace("\n","") for req in requirements]

        if const in requirements:
            requirements.remove(const)

    return requirements



setup(
    name="ml_project",  # Name of the package
    version="0.0.1",  # Package version
    author="sannabewaga",
    author_email="gauravsarthak00@gmail.com",
    description="A short description of the project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",  # Project URL
    packages=find_packages(),  # Automatically finds and includes packages
    install_requires=get_requirements('requirements.txt')
)
