import io

from setuptools import find_packages, setup
from os.path import dirname, abspath, join


with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

base_path = dirname(abspath(__file__))

with open(join(base_path, "requirements.txt")) as req_file:
    requirements = req_file.readlines()

setup(
    name="asu",
    version="0.3.0",
    url="https://github.com/aparcar/asu",
    maintainer="Paul Spooren",
    maintainer_email="mail@aparcar.org",
    description="Create images for OpenWrt on demand",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
)
