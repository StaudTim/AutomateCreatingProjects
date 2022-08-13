# Automate the process of creating a new project

This project automates the process of creating a new project by doing the following steps:

1. Navigate into directory where you store your projects
2. Create a new repository on GitHub
3. Clone the repository into your directory
4. Create and open README and main file



## Table of Contents

- [Install](#install)
- [Setup](#setup)
- [Usage](#usage)



## Install

The "requests" package is needed:

```sh
$ pip install requests
```



## Setup

You have to add "config.json" which contains your access token from GitHub. An example is given in "config_example.json".


## Usage

Simply enter the command "createProject" in the command line. In addition, two parameters must also be passed:

1. Name of the project
2. Type of the main file (Example: py for a python file)

```sh
$ createProject myProject py
```
