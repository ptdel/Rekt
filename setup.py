import os
from setuptools import setup, find_packages
from typing import List

cwd = os.path.abspath(os.path.dirname(__file__))

requires: List[str] = ["boto3", "discord", "toml"]

setup(
    name="Rekt",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="Rekt",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=requires,
)
