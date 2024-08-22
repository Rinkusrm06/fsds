from setuptools import find_packages, setup

Hyphen_e_dot ='-e .'

def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Rinku Sharma',
    author_email='rinkusrm0@gmail.com',
    packages=find_packages()
)