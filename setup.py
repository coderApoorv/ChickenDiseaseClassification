import setuptools

with open('Readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_Name = 'ChickenDiseaseClassification'
AUTHOR_USER_NAME = 'Apoorv'
SRC_REPO = 'ChickenDiseaseClassification'
AUTHOR_EMAIL = 'apoorvj6@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for CNN app',
    Long_description = long_description,
    Long_description_content = 'text/markdown',
    url= f'https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}',
    project_urls ={
        'Bug Trcaker':f'https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}/issues'
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)