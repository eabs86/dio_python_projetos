from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    

setup(
    name='image_processing_dio_eabs86',
    version='0.0.3',
    author='Emmanuel Andrade',
    author_email='emmanuel.andrade@gmail.com',
    description='Pacote criado durante o bootcamp Python Developer da DIO',
    long_description= page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/eabs86/dio_python_projetos/tree/master/Processamento_de_Imagem/image-processing-package-dio-eabs86',
    packages= find_packages(),
    install_requires = requirements,
    python_requires = '>=3.8'
    
)