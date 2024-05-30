from setuptools import setup, find_packages 

setup(
    name='foo_param',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'calculate_sphere_volume=examples.example_usage:main',
        ],
    },
)
