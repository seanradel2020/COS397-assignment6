![testpypi](https://github.com/seanradel2020/COS397-assignment6/actions/workflows/python-app.yml/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/seanradel2020/COS397-assignment6)
# DevOps Exercise - Assignment 6 - COS 397 - Fall 2023
Authors: Sean Radel, Gabe Poulin, Brennan Poitras, Collin Rodrigue, Graham Bridges

Our testing strategy combines Github workflows and pre-commit testing with [pre-commit](https://pre-commit.com/).
When a developer is ready to push their changes to our repository, the following steps are completed: 
1. First the developer adds their files to stage changes
    1. git add "filename"
2. Next, the developer commits their changes
    1. git commit -m "commit message"
    2. This kicks off our pre-commit tests, as specified in the file ".pre-commit-config.yaml". 
    3. pre-commit ensures the code passes the following tests: 
        1. check for added large file
        2. detect private key
        3. detect aws credentials
    4. pre-commit ensures the code conforms to the following style checkers and linters:
        1. black
        2. flake8
3. Next, using GitHub actions, you can start the workflow manually.
    1. This workflow "Python Application" complies a package for MacOS, Windows and Ubuntu, all the latest versions.
    2. This workflow also runs PyTest on the Ubuntu package, as that is the most recent one created, which runs all tests presented in the tests folder.
    3. Finally, the workflow, using a generated API key in secrets, sends the package to TestPyPi, where you can use pip to install our package. 


1. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
1. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  


