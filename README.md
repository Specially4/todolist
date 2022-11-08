# TODOLIST

## Stack

* ![version](https://img.shields.io/badge/Poetry-v1.2.2-informational/?style=for-the-badge&logo=Poetry)
* ![version](https://img.shields.io/badge/Python-v3.10.6-informational/?style=for-the-badge&logo=Python)
* ![version](https://img.shields.io/badge/Django-v4.1.3-informational/?style=for-the-badge&logo=Django)
* ![version](https://img.shields.io/badge/Postgresql-v15.0-informational/?style=for-the-badge&logo=Postgresql)

## Install

### Clone the repo

```sh
git clone
```

### Install dependency manager

_Windows_

```sh
pip install poetry
```

_Mac/Linux_

```sh
pip3 install poetry
```

### Install dependencies

_All_

```sh
poetry init
poetry install
```

### Start DB

```sh
docker-compose up --build -d
```

### Roll up migrations

_Windows_

```sh
python manage.py migrate
```

_Mac/Linux_

```sh
./manage.py migrate
```

### Run app

_Windows_

```sh
python manage.py runserver
```

_Mac/Linux_

```sh
./manage.py runserver
```