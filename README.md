# Cape Technical Test 
## WIFI Access Point Scan Based Geolocation-API

## Requirements
- Python 3.9+
- PostgreSQL 9.6+

Please consult Google if you need to install any of the pre-requisites

## Set Up Installation
- Clone/Download the git repo - `git clone https://github.com/Mhlengi/cape_technical_test_wifi_access_point.git`
- Create a Postgres database `wifi_access_point_scan` with user `postgres` and password `postgres`
- Navigate to the project folder`cape_technical_test_wifi_access_point`
- Install python3 `brew install python3`
- Install pip3 `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv`
- Activate a virtual environment: `. venv/bin/activate`
- Install all the python dependencies `pip install -r requirements.txt`
- Run the database migrations `python manage.py migrate`
- Run collect static files `python manage.py collectstatic`
- Create Superuser but not required for this tasks `python manage.py createsuperuser` 
- Start the WebServer `python manage.py runserver`
(*Please note everytime you pull from master you may need to run the migrations and install any new dependencies
- as per the above instructions*)
- Note: please find `config.py` file in source folder. 
- Then update your `GOOGLE_API_KEY = "******************************************"`. 
- Which can be found here [google developer console documentation](https://developers.google.com
/maps/documentation/geolocation/get-api-key) or Find it from your development team.

### Running django pytest
`py.test -xvv --create-db`.

### Running django pytest with code-coverage report
`coverage run -m py.test -xvv --create-db; coverage html; coverage report;`

### Test Localhost Browser Application
- Access swagger docs [localhost home application](http://localhost:8000/) on your browser.

![localhost home application](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/SwaggerScreenshot.png)

- Access django admin [localhost admin application](http://localhost:8000/admin/) on your browser.
Note: [localhost admin application](http://localhost:8000/admin/) requires admin superuser
 credentials.

![localhost admin application](https://github.com/Mhlengi/cape_technical_test_wifi_access_point
/blob/master/AdminScreenshot.png)

