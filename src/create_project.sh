#!/bin/bash

function createProject() {
  # create repository
  cd
  cd Desktop/Repository.nosync/AutomateCreatingProjects/src
  python repository.py $1

  # clone repository
  cd
  cd Desktop/Repository.nosync
  git clone https://github.com/StaudTim/$1.git
  cd $1

  # readme
  touch README.md
  open README.md

  # src
  mkdir src
  cd src
  touch $1.py
  open $1.py
}