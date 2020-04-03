# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project.
The console can be used to store objects in and retrieve objects either from a JSON
or from MySQL database.

## Topics
Several concepts from **Software engineering** are applied:
- What is Unit testing and how to implement it in a large project (TDD)
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables

## The project
Next what do you need tu use it and learn about it:

### Requirements:
* Ubuntu 14.04 LTS
* python3 (version 3.4.3)
* MySQL 5.7 (version 5.7.8-rc)
* MySQLdb module version 1.3.x
* SQLAlchemy version 1.2.x

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

### Usage:
To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

#### Aditional:
Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

### Examples:
You can verify the software in the next way:

#### 1. Bug free!
Do you remember the unittest module?

```bash wrap
guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null
.....................ss......
OK
guillaume@ubuntu:~/AirBnB_v2$ 
```

```bash wrap
guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null
ss....s...............ss......
OK
guillaume@ubuntu:~/AirBnB_v2$
```

## Authors
* Miranda Evans - miranda.r.evans@gmail.com
* Kevin Yook - kevin.yook@holbertonschool.com
* Hugo Bayona - hugo.bayona@holbertonschool.com
* Gonzalo Gomez Millan - 1240@holbertonschool.com
