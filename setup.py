from setuptools import setup, find_packages

setup(
    name='dev_api',
    version='1.0.0',
    description='API para consumo de Blog Frontend',
    url='',

    classifiers=[
        'Programming Language :: Python :: 3.10'
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.13.0', 'Flask-SQLAlchemy==1.4.43'],
)
