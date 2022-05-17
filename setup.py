import pathlib
import pkg_resources
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.1'
PACKAGE_NAME = 'neural_response_map'
AUTHOR = 'Joan Alberto Cerretani'
AUTHOR_EMAIL = 'joancerretani@gmail.com'
URL = 'https://github.com/joancerretani'

LICENSE = 'MIT'
DESCRIPTION = 'Library to visualize the activations of the hidden layers of artificial neural networks'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

with pathlib.Path('requirements.txt').open() as requirements_txt:
    INSTALL_REQUIRES = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)