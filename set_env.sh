#!/bin/bash
#
# This shell set the environment for the AirBnBclone - MySQL project
#
# Authors
# =======
# Hugo Bayona - hugo.bayona@holbertonschool.com
# Gonzalo Gomez Millan - 1240@holbertonschool.com
#
# Usage:
#   (1) source ./set_env.sh [test|dev] [file|db]
#   or
#   (2) . ./set_env.sh [test|dev] [file|db]
#
#   test : for test environment
#   dev  : for development environment
#   file : for using FileStorage
#   db   : for using DBStorage
#

set_env () {
  if [ $# -lt 2 ]
  then
    echo "--" >&2
    printf "%s: Error: Invalid number of arguments.\n" "$0" >&2
    echo "Usage: source ./set_env.sh [test|dev] [file|db]" >&2
    echo "       or" >&2
    echo "       . ./set_env.sh [test|dev] [file|db]" >&2
    return 1
  fi

  if [[ $1 =~ ^TEST$|^test$ ]]
  then
    export HBNB_ENV="test"
    export HBNB_MYSQL_DB="hbnb_test_db"
    export HBNB_MYSQL_USER="hbnb_test"
    export HBNB_MYSQL_PWD="hbnb_test_pwd"
  elif [[ $1 =~ ^DEV$|^dev$ ]]
  then
    export HBNB_ENV="dev"
    export HBNB_MYSQL_DB="hbnb_dev_db"
    export HBNB_MYSQL_USER="hbnb_dev"
    export HBNB_MYSQL_PWD="hbnb_dev_pwd"
  else
    echo "--" >&2
    printf "%s: Error: (%s) is an invalid argument.\n\n" "$0" "$1" >&2
    echo "Usage: source ./set_env.sh [test|dev] [file|db]" >&2
    echo "       or" >&2
    echo "       . ./set_env.sh [test|dev] [file|db]" >&2
    return 1
  fi

  if [[ $2 =~ ^FILE$|^file$ ]]
  then
    export HBNB_TYPE_STORAGE="file"
  elif [[ $2 =~ ^DB$|^db$ ]]
  then
    export HBNB_TYPE_STORAGE="db"
  else
    echo "--" >&2
    printf "%s: Error: (%s) is an invalid argument.\n\n" "$0" "$2" >&2
    echo "Usage: source ./set_env.sh [test|dev] [file|db]" >&2
    echo "       or" >&2
    echo "       . ./set_env.sh [test|dev] [file|db]" >&2
    return 1
  fi

  export HBNB_MYSQL_HOST="localhost"

  return 0
}

set_env "$1" "$2"
