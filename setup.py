from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Painy",
    version="0.1.1",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raevskiy Rudolf",
    url="https://github.com/lanesket/painy",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            "painy = painy.main:main"
        ]
    }
)