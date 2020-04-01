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
if [ $# -lt 2 ]
then
  echo "--" >&2
  echo "$0: Error: Invalid number of arguments.\n" >&2
  echo "Usage: source ./set_env.sh [test|dev] [fs|dbs]" >&2
  echo "       or" >&2
  echo "       . ./set_env.sh [test|dev] [fs|dbs]" >&2
  exit 1
fi

if [[ $1 =~ ^TEST|test$ ]]
then
  export HBNB_ENV="test"
  export HBNB_MYSQL_DB="hbnb_test_db"
  export HBNB_MYSQL_USER="hbnb_test"
  export HBNB_MYSQL_PWD="hbnb_test_pwd"
elif [[ $1 =~ ^DEV|dev$ ]]
then
  export HBNB_ENV="dev"
  export HBNB_MYSQL_DB="hbnb_dev_db"
  export HBNB_MYSQL_USER="hbnb_dev"
  export HBNB_MYSQL_PWD="hbnb_dev_pwd"
else
  echo "--" >&2
  echo "$0: Error: ($1) is an invalid argument.\n" >&2
  echo "Usage: source ./set_env.sh [test|dev] [fs|dbs]" >&2
  echo "       or" >&2
  echo "       . ./set_env.sh [test|dev] [fs|dbs]" >&2
  exit 1
fi

if [[ $2 =~ ^FILE|file$ ]]
then
  echo "file - $2"
  export HBNB_TYPE_STORAGE="file"
elif [[ $2 =~ ^DB|db$ ]]
then
  echo "db - $2"
  export HBNB_TYPE_STORAGE="db"
else
  echo "$0: Error: ($2) is an invalid argument." >&2
  echo "Usage: source ./set_env.sh [test|dev] [file|db]" >&2
  exit 1
fi

export HBNB_MYSQL_HOST="localhost"

exit 0
