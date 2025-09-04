from setuptools import setup, find_packages

setup(
    name="ma2003b-course",
    version="1.2.0",
    description="MA2003B course materials and utilities",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
)
