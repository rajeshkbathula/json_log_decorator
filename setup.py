import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='json_log_decorator',
    version='1.2.0',
    author="Rajesh Bathula",
    author_email="rajb2237@gmail.com",
    description="The Python LogDecorator with exception, in JSON format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rajeshkbathula/json_log_decorator",
    packages=["json_log_decorator"] or setuptools.find_packages(),
    install_requires=["python-json-logger==2.0.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)