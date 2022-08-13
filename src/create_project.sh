#!/bin/bash

function createProject() {
  if [ $# -eq 2 ]; then

    # create repository
    cd
    cd Desktop/Repository.nosync/AutomateCreatingProjects/src
    python repository.py $1

    # clone repository
    cd
    cd Desktop/Repository.nosync
    git clone https://github.com/StaudTim/$1.git

    # readme
    cd $1
    touch README.md
    open README.md

    # src
    mkdir src
    cd src
    touch main.$2
    open main.$2

  else
    echo "supply arguments: 1) name of the project 2) file type (py, r)"

  fi
}
