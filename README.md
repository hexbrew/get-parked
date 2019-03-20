# get-parked

## Installation

#### Make a virtual environment inside the repo directory
https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
make sure to call it env

#### Activate it
```
source env/bin/activate
```

#### Install dependencies for Django and run
```
cd getparked
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

#### Install node modules and run React
```
cd frontend
npm i
npm run start
```
