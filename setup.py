from setuptools import setup, find_packages

setup(
    name='comfydl',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'comfydl': ['model_sources/*.yaml'],
    },
    install_requires=[
        'PyYAML',
        'requests',
        'tqdm',
        'questionary',
    ],
    entry_points={
        'console_scripts': [
            'comfydl=comfydl.main:main',
        ],
    },
)
