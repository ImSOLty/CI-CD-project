#!/bin/bash

CYAN='\033[0;36m'
NC='\033[0m' # No Color

TESTS_FOLDER='/devops-examples/EXAMPLE_APP/tests'

# Create folder if not exist
mkdir -p ${TESTS_FOLDER}/test_results;


function code_style_tests {
  echo -e "${CYAN}CODE STYLE TESTS${NC}";
  # run yapf style tests
  yapf -ir -vv --style=pep8 . \
   > >(tee -a ${TESTS_FOLDER}/test_results/stdout.log) 2> >(tee -a ${TESTS_FOLDER}/test_results/stderr.log >&2) &> >(tee -a /proc/1/fd/1);
  # output to stderr, stdout and 1 process
}

function pylint_tests {

  touch __init__.py; # pylint requires the __init__.py file to exist in target directory

  echo -e "${CYAN}PYLINT 10 TESTS${NC}";
  # run pylint with 10 enabled
  pylint $(pwd) -v --rcfile=${TESTS_FOLDER}/pylintrc \
   > >(tee -a ${TESTS_FOLDER}/test_results/stdout.log) 2> >(tee -a ${TESTS_FOLDER}/test_results/stderr.log >&2) &> >(tee -a /proc/1/fd/1);

  echo -e "${CYAN}PYLINT CUSTOM CRITERIA TEST${NC}";
  # run pylint with custom name criteria
  pylint $(pwd) -v --rcfile=${TESTS_FOLDER}/pylintrc_custom \
   > >(tee -a ${TESTS_FOLDER}/test_results/stdout.log) 2> >(tee -a ${TESTS_FOLDER}/test_results/stderr.log >&2) &> >(tee -a /proc/1/fd/1);

  rm __init__.py; # remove added __init__.py
}

function integration_tests {
  echo -e "${CYAN}INTEGRATION TESTS${NC}";
  # run tests with integration_tests marker from integration_tests.py script
  pytest -s -v --tb=line -m integration_tests ${TESTS_FOLDER}/integration_tests.py \
   > >(tee -a ${TESTS_FOLDER}/test_results/stdout.log) 2> >(tee -a ${TESTS_FOLDER}/test_results/stderr.log >&2) &> >(tee -a /proc/1/fd/1);
}

function selenium_tests {
  echo -e "${CYAN}SELENIUM TESTS${NC}";
  # run tests with selenium_tests marker from selenium_tests.py script
  pytest -s -v --tb=line -m selenium_tests -c ${TESTS_FOLDER}/pytest.ini ${TESTS_FOLDER}/selenium_tests \
   > >(tee -a ${TESTS_FOLDER}/test_results/stdout.log) 2> >(tee -a ${TESTS_FOLDER}/test_results/stderr.log >&2) &> >(tee -a /proc/1/fd/1);
  # screenshots from selenium are placed under <project_directory>/tests/test_results
}

if [ $# -eq 0 ]
  then
    code_style_tests
    pylint_tests
    integration_tests
    selenium_tests
  else
    $1
fi