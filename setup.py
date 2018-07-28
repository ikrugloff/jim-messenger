from setuptools import setup

setup(
    name="dagobah-messenger",
    version='0.1',
    description='JIM socket messenger',
    long_description='JSON instant messenger with presence control and AES encryption',
    url='https://github.com/ikrugloff/jim-messenger',
    license='MIT',
    keywords=['python', 'messenger', 'json', 'jim', 'geekbrains'],
    author='Ilia Kruglov',
    packages=['jim-messenger', 'jim-messenger/ui'],
    include_package_data=True,
    python_requires='>=3.6.5',
    install_requires=[
        'PyQt5==5.11.2', 
        'SQLAlchemy==1.2.10',
        'pycryptodome==3.6.4',
        'pycryptodomex==3.6.4'
    ],
)