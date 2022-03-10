# receipt_generator_api

This is a Django web application that generate receipt for users. 

TECHNOLOGIES
The following technologies were used in this project:
Python
Django
Django REST Framework
SQLite 3 (local)
postegrs(heroku)


# Getting Started
To run this application locally:
- Open up terminal (on MacOS) and switch directory to Desktop by running:
```
cd ~
```
- For Windows, open git bash and switch directory to Desktop by running:
```
cd Desktop
```
- Clone the repository by running:
```
git clone https://github.com/Adeakim/receipt_generator_api.git
```
- Then run the following commands consecutively
```
cd receipt_generator_api
```
```
python3 -m venv venv 
```
- To activate virtual environment (MacOS users): 
```
source venv/bin/activate
```
- To activate virtual environment (Windows users):
```
source venv/Source/activate
```
- Install dependencies as follows (both MacOS & Windows):
```
pip install -r requirements.txt
```
- Make migrations by running the commands below in succession:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- To start the Django server, run:
```
python manage.py runserver
```
-Navigate to ```http://127.0.0.1:8000/```

This will show the API documentation on swagger.

<!-- .................................TESTING THE ENDPOINTS........................................................... -->

<!-- Register a user -->
METHOD : POST
ROUTE:  api/v1/auth/register
ON LOCALHOST: http://127.0.0.1:8000/api/v1/auth/register
PAYLOAD:
{
  "name": "string",
  "email": "user@example.com",
  "mobile_number": "string", #format +999999999999
  "address": "string",
  "password": "string",
  "confirm_password": "string"
}
RESPONSE FORMAT

{
  "message": "success",
  "data":
  {
  "name": "string",
  "email": "user@example.com",
  "mobile_number": "string",
  "address": "string",
  "password": "string",
  "confirm_password": "string"
}
  "errors": { null
  }
  
 
 <!-- Sign in  a user -->
METHOD : POST
ROUTE:  api/v1/auth/login
ON LOCALHOST: http://127.0.0.1:8000/api/v1/auth/login
PAYLOAD:
{
  "email": "user@example.com",
  "password": "string"
}
RESPONSE FORMAT

{
  "message": "success",
  "data": 
  { "token": "bearer access token"
}
  "errors": { null
  }
<!-- Generate a receipt for a user -->
METHOD : POST
ROUTE:  api/v1/generate-receipt
ON LOCALHOST: http://127.0.0.1:8000/api/v1/generate-receipt
PAYLOAD:
{
  "user": "user@example.com",
  "total_amount_payable": <float>
}
RESPONSE FORMAT

{
  "message": "success",
  "data": 
  { "pdf_url": "url to the pdf"
}
  "errors": { null
  }

<!-- Get all generated receipts -->
METHOD : GET  
ROUTE:  api/stories/<uuid:id>
ON LOCALHOST: http://127.0.0.1:8000/api/stories/cd182687-e0f0-4f5b-9f3c-dde735f0818b/

RESPONSE FORMAT
{
    "message": "success",
    "data": {
        "receipt": [
            {
                "name": "",
                "mobile_number": "",
                "address": "",
                "total_amount_payable": ""
            },
            {
                "name": "",
                "mobile_number": "",
                "address": "",
                "total_amount_payable": ""
            },
            {
                "name": "",
                "mobile_number": "",
                "address": "",
                "total_amount_payable": ""
            },
            ],
        "total": 3
    },
    "errors": null
}
