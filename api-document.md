### Accessing the API

#### Generate Access Token
To get access to API functionalities, Generate Access Token from the below POST API 
```bash
http://127.0.0.1:5000/auth
```
with the username and password created at [security.py](https://github.com/manikandanvaidy/customers-api/blob/master/security.py)

>curl --location --request POST 'http://127.0.0.1:5000/auth' \
--header 'Content-Type: application/json' \
--data-raw '{
"username": "USERNAME",
"password": "PASSWORD"
}'

#### Get all users API
This API is used to fetch all the users in the database
```bash
http://127.0.0.1:5000/api/Customer
```
Pass the Access Token in the Authorization header with the below format using GET method
>curl --location --request GET 'http://127.0.0.1:5000/api/Customer' \
--header 'Authorization: JWT ACCESS_TOKEN' \
--header 'Content-Type: application/json'

#### Get N number of youngest users list API
This API is used to fetch all the n number youngest users in the database with the n value passed
```bash
http://127.0.0.1:5000/api/Customer/:number
```
Pass the Access Token in the Authorization header and number of youngest users with the below format using GET method
>curl --location --request GET 'http://127.0.0.1:5000/api/Customer/:number' \
--header 'Authorization: JWT ACCESS_TOKEN' \
--header 'Content-Type: application/json'

#### Create user API
This API is used to create a new user with DOB in the database
```bash
http://127.0.0.1:5000/api/Customer
```
Pass the Access Token in the Authorization header, user's name and DOB with the below format using POST method
>curl --location --request POST 'http://127.0.0.1:5000/api/Customer' \
--header 'Authorization: JWT ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "User Name",
"dob" : "2007-12-03T00:00:00"
}'

#### Update user API
This API is used to update a user's name and DOB in the database
```bash
http://127.0.0.1:5000/api/Customer
```
Pass the Access Token in the Authorization header, user's name, DOB and User ID with the below format using PUT method
>curl --location --request PUT 'http://127.0.0.1:5000/api/Customer' \
--header 'Authorization: JWT ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "New name",
"dob" : "2017-12-03T00:00:00",
"id" : 3
}'

#### Delete user API
This API is used to delete a user in the database
```bash
http://127.0.0.1:5000/api/Customer
```
Pass the Access Token in the Authorization header and User ID with the below format using DELETE method
>curl --location --request DELETE 'http://127.0.0.1:5000/api/Customer' \
--header 'Authorization: JWT ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
"id" : 3
}'