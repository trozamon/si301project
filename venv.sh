#!/bin/sh

VENV_DIR="../si301project.venv"

test -d ${VENV_DIR} || virtualenv ${VENV_DIR}
source ${VENV_DIR}/bin/activate
pip install -r requirements.txt
