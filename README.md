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
- Note: Please find `config.py` file in source folder. 
- Then update your `GOOGLE_API_KEY = "******************************************"` 
- Which can be found here [google developer console documentation](https://developers.google.com/maps/documentation/geolocation/get-api-key) or Find it from your development team

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

![localhost admin application](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/AdminScreenshot.png)

### Application Demo or REST-API usage
`To demonstrate REST-API's, One can choose any of the REST-API clients (Example: Postman, Curl Terminal, httpie, Swagger docs, etc).`
- For this demo, our REST-API client is `Postman`


### Before Demonstration
### The Project Outline & Requirements
- Outline
- `We would like you to create a service that accepts Wi-Fi access point (AP) scan result data and
 returns the latitude and longitude of the location at which the AP scan was performed. This is a real service that currently exists within our architecture.`

- Requirements
- `
We would like the solution to be a REST API (use any language you want). It needs to accept a single batch of AP scan data of the format:
`

- ![localhost admin application](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/InputDataScreenshot.png)

- `And it needs to return a response in the format:`

- ![localhost admin application](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/OutputScreenshot.png)

### Postman Demo REST-APIs client
- To create a new WIFI access point scan use `POST` http Method.
- `POST API` endpoint `http://127.0.0.1:8000/api/v1/apscan/add/`

- ![POST API](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/POSTScreenshot.png)


- To list all WIFI access point scan that are already added in DB, use `GET` http Method.
- `GET API` endpoint `http://127.0.0.1:8000/api/v1/apscan/all/`

- ![GET API](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/GETAllScreenshot.png)


- To retrieve a single WIFI access point scan that is already added in DB, use `GET` http Method.
- DB object pk/id required, For this demo `pk/id=5` 
- `GET API` endpoint `http://127.0.0.1:8000/api/v1/apscan/5/retrieve/`

- ![GET API](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/GETSingleScreenshot.png)


- To edit a single WIFI access point scan that is already added in DB, use `PUT` http Method.
- DB object pk/id required, For this demo `pk/id=5` 
- `PUT API` endpoint `http://127.0.0.1:8000/api/v1/apscan/5/edit/`

- ![PUT API](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/PUTScreenshot.png)


- To delete a single WIFI access point scan that is already added in DB, use `DELETE` http Method.
- DB object pk/id required, For this demo `pk/id=5` 
- `DELETE API` endpoint `http://127.0.0.1:8000/api/v1/apscan/5/delete/`

- ![DELETE API](https://github.com/Mhlengi/cape_technical_test_wifi_access_point/blob/master/DELETEScreenshot.png)
