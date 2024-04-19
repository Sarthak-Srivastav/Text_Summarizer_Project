import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text_Summarizer_Project"
Author_Name = "Sarthak-Srivastav"
SRC_REPO = "Text_Summarizer"
Author_Email = "the.sarthak.boy@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_Name,
    author_email=Author_Email,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_Name}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_Name}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)