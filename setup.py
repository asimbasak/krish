from setuptools import setup, find_packages

setup(
    name="krish",
    version="0.1",
    packages=find_packages(),
    description="A simple Python package related to Vibration data analysis",
    author="Asim Basak",
    author_email="basak.asim.cs@gmail.com",
    url="https://github.com/asimbasak/krish",
    license="MIT",
    install_requires=[
        "pandas>=1.0.0"
    ],
    python_requires='>=3.6',
)
