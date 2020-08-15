import setuptools
from os import path
def get_long_description():
    with open(
        path.join(path.dirname(path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as f:
        return f.read()

setuptools.setup(
    name="streamlit-observable",
    version="0.0.1",
    author="Alex Garcia",
    description="A Streamlit Component for embeding Observable Notebooks in Streamlit Apps",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/asg017/streamlit-observable",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)