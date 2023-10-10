from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in technology/__init__.py
from technology import __version__ as version

setup(
	name="technology",
	version=version,
	description="it is a demo app",
	author="quantibit",
	author_email="w",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
