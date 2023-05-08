from setuptools import find_packages, setup

setup(
    name='saluda',
    version='0.1.0', 
    description="aprendiendo acerca de los paquetes distribuibles ejecutables.",
    author="Jaime Feldman", 
    license='MIT', 
    long_description_content_type='text/markdown',
    url='https://github.com/jaimefeldman/prueba',
    packages=find_packages(exclude=('test*', 'testing*')),
    include_package_data=True,
    install_requires=[
        'termcolor==2.1.0'
    ],
    entry_points={
        'console_scripts': [
            'saluda = saludador.launcher.__main__:main',
        ]
    },
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: MacOS",
     ],
)

