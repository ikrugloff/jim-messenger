import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
	README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="dagobah-messenger",
    version='0.1',
    description='JIM socket messenger',
    long_description=README,
    url='https://github.com/ikrugloff/jim-messenger',
    license='GNU General Public License v3.0',
    keywords=['python', 'messenger', 'json', 'jim', 'geekbrains'],
    author='Ilia Kruglov',
    include_package_data=True,
    python_requires='>=3.6.5',
    install_requires=[
        'PyQt5==5.11.2', 
        'SQLAlchemy==1.2.10',
        'pycryptodome==3.6.4',
        'pycryptodomex==3.6.4'
    ],
    entry_points={
    	'console_scripts': [
    		'dagobah-srv = server.main:main',
    		'dagobah-cli = clnt_cli.main:main'
    	],
    	'gui_scripts': [
    		'dagobah-gui = clnt_gui.main:main'
    	]
    },
)