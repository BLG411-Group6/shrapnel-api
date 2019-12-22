Create Poll
-----------------

Method: **POST**

Endpoint: **/api/polls/**

Example Request::

    POST /api/polls/
        {
            "title": "Best Food",
            "options": [
                {
                    "body": "Pizza"
                },
                {
                    "body": "Hamburger"
                }
            ],
            "date_expiration": "2019-12-27T23:27:17.895665+03:00"
        }

Example Response::

    HTTP 201 CREATED
    {
        "id": 18,
        "title": "Best Food",
        "user": {
            "id": 1,
            "username": "baran"
        },
        "options": [
            {
                "id": 37,
                "body": "Pizza",
                "number_of_answers": 0,
                "date_created": "2019-12-22T15:21:09+0000"
            },
            {
                "id": 38,
                "body": "Hamburger",
                "number_of_answers": 0,
                "date_created": "2019-12-22T15:21:09+0000"
            }
        ],
        "date_created": "2019-12-22T15:21:09+0000",
        "date_expiration": "2019-12-27T20:27:17+0000"
    }


List Polls
-----------------

Method: **GET**

Endpoint: **/api/polls/**

Example Request::

    GET /api/polls/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 6,
            "title": "Best Movies",
            "user": {
                "id": 1,
                "username": "baran"
            },
            "options": [
                {
                    "id": 7,
                    "body": "GoodFellas",
                    "number_of_answers": 2,
                    "date_created": "2019-12-22T08:10:38+0000"
                },
                {
                    "id": 8,
                    "body": "Casino",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T08:10:38+0000"
                },
                {
                    "id": 9,
                    "body": "Taxi Driver",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T08:10:38+0000"
                }
            ],
            "date_created": "2019-12-22T08:10:38+0000",
            "date_expiration": "2019-12-27T20:27:17+0000"
        },
        {
            "id": 11,
            "title": "Best Food",
            "user": {
                "id": 1,
                "username": "baran"
            },
            "options": [
                {
                    "id": 17,
                    "body": "Pizza",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T09:51:51+0000"
                },
                {
                    "id": 18,
                    "body": "Hamburger",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T09:51:51+0000"
                }
            ],
            "date_created": "2019-12-22T09:51:51+0000",
            "date_expiration": "2019-12-27T20:27:17+0000"
        },
    ]


Get Poll Detail
-----------------

Method: **GET**

Endpoint: **/api/polls/<id>/**

Example Request::

    GET /api/polls/6/

Example Response::

    HTTP 200 OK
    {
        "id": 6,
        "title": "Best Movies",
        "user": {
            "id": 1,
            "username": "baran"
        },
        "options": [
            {
                "id": 7,
                "body": "GoodFellas",
                "number_of_answers": 2,
                "date_created": "2019-12-22T08:10:38+0000"
            },
            {
                "id": 8,
                "body": "Casino",
                "number_of_answers": 0,
                "date_created": "2019-12-22T08:10:38+0000"
            },
            {
                "id": 9,
                "body": "Taxi Driver",
                "number_of_answers": 0,
                "date_created": "2019-12-22T08:10:38+0000"
            }
        ],
        "date_created": "2019-12-22T08:10:38+0000",
        "date_expiration": "2019-12-27T20:27:17+0000"
    }


Update Poll
-----------

Method: **PATCH**

Endpoint: **/api/polls/<id>/**

Example Request::

    PATCH /api/polls/9/
    {
        "title": "Updated Title",
    }

Example Response::

    HTTP 200 OK
    {
        "id": 6,
        "title": "Updated Title",
        "user": {
            "id": 1,
            "username": "baran"
        },
        "options": [
            {
                "id": 7,
                "body": "GoodFellas",
                "number_of_answers": 2,
                "date_created": "2019-12-22T08:10:38+0000"
            },
            {
                "id": 8,
                "body": "Casino",
                "number_of_answers": 0,
                "date_created": "2019-12-22T08:10:38+0000"
            },
            {
                "id": 9,
                "body": "Taxi Driver",
                "number_of_answers": 0,
                "date_created": "2019-12-22T08:10:38+0000"
            }
        ],
        "date_created": "2019-12-22T08:10:38+0000",
        "date_expiration": "2019-12-27T20:27:17+0000"
    }


Delete Poll
-----------------

Method: **DELETE**

Endpoint: **/api/polls/<id>/**

Example Request::

    DELETE /api/polls/9/

Example Response::

    HTTP 204 NO CONTENT


Create Poll Option
------------------
Method: **POST**

Endpoint: **/api/polls/<poll_id>/options/**

Example Request::

    POST /api/polls/6/options/
    {
        "body": "The Irishman"
    }

Example Response::

    HTTP 201 CREATED
    {
        "id": 39,
        "body": "The Irishman",
        "number_of_answers": 0,
        "date_created": "2019-12-22T15:41:50+0000"
    }

List Poll Options
-----------------
Method: **GET**

Endpoint: **/api/polls/<poll_id>/options/**

Example Request::

    GET /api/polls/6/options/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 7,
            "body": "GoodFellas",
            "number_of_answers": 2,
            "date_created": "2019-12-22T08:10:38+0000"
        },
        {
            "id": 8,
            "body": "Casino",
            "number_of_answers": 0,
            "date_created": "2019-12-22T08:10:38+0000"
        },
        {
            "id": 9,
            "body": "Taxi Driver",
            "number_of_answers": 0,
            "date_created": "2019-12-22T08:10:38+0000"
        }
    ]


Answer Poll (Vote)
------------------
Method: **POST**

Endpoint: **api/polls/<poll_id>/options/<option_id>/answer**

Example Request::

    POST /api/polls/6/options/39/answer

Example Response::

    {
        "id": 12,
        "user": {
            "id": 6,
            "username": "voter"
        },
        "poll": {
            "id": 6,
            "title": "Updated Title",
            "user": {
                "id": 1,
                "username": "baran"
            },
            "options": [
                {
                    "id": 7,
                    "body": "GoodFellas",
                    "number_of_answers": 2,
                    "date_created": "2019-12-22T08:10:38+0000"
                },
                {
                    "id": 8,
                    "body": "Casino",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T08:10:38+0000"
                },
                {
                    "id": 9,
                    "body": "Taxi Driver",
                    "number_of_answers": 0,
                    "date_created": "2019-12-22T08:10:38+0000"
                },
                {
                    "id": 39,
                    "body": "The Irishman",
                    "number_of_answers": 1,
                    "date_created": "2019-12-22T15:41:50+0000"
                }
            ],
            "date_created": "2019-12-22T08:10:38+0000",
            "date_expiration": "2019-12-27T20:27:17+0000"
        },
        "option": {
            "id": 39,
            "body": "The Irishman",
            "number_of_answers": 1,
            "date_created": "2019-12-22T15:41:50+0000"
        },
        "date_created": "2019-12-22T15:53:45+0000",
        "date_updated": "2019-12-22T15:53:45+0000"
    }

