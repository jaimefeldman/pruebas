from setuptools import find_packages, setup

setup(
    name='prueba',
    version='0.1.0', 
    description="aprendiendo acerca de los paquetes distribuibles ejecutables.",
    author="Jaime Feldman", 
    license='MIT', 
    long_description_content_type='text/markdown',
    url='https://github.com/jaimefeldman/prueba',
    packages=find_packages(exclude=('test*', 'testing*')),
    install_requires=[
        'termcolor==2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'prueba = launcher.__main__:main',
        ]
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: MacOS",
     ],
)

