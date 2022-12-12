from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "NLP-DVC-Project"
AUTHOR_NAME = "Shivansh Kaushal"
AUTHOR_USER_NAME = "shivanshka"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    description="Stackoverflow Python Tags Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.git",
    author_email="kaushal.shivansh630@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
