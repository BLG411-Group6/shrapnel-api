Registration
------------
Method: **POST**

Endpoint: **/api/users/register**

Example Request::

    POST /api/users/register/
    {
        "email": "testuser@shrapnel.com",
        "username": "testusername",
        "first_name": "Test",
        "last_name": "User",
        "password": "password",
        "repeated_password": "password"
    }

Example Response::

    HTTP 201 CREATED
    {
        "id": 3,
        "username": "testusername",
        "email": "testuser@shrapnel.com",
        "first_name": "Test",
        "last_name": "User"
    }


Login
-----
Method: **POST**

Endpoint: **/api/users/login**

Example Request::

    POST /api/users/login/
    {
        "username": "username",
        "password": "password"
    }

Example Response::

    HTTP 204 NO CONTENT


Logout
------
Method: **GET**

Endpoint: **/api/users/logout**

Example Request::

    GET /api/users/logout/

Example Response::

    HTTP 204 NO CONTENT
