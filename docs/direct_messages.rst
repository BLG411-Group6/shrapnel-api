List Receivers
-----------------

Method: **GET**

Endpoint: **/api/direct-messages/receivers/**

Example Request::

    GET /api/direct-messages/receivers/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 3,
            "username": "username3"
        },
        {
            "id": 2,
            "username": "username2"
        },
        {
            "id": 4,
            "username": "username4"
        }
    ]


Send Direct Message
-----------------

Method: **POST**

Endpoint: **/api/direct-messages/send/**

Example Request::

    POST /api/direct-messages/receivers/
    {
        "title": "message_title",
        "content": "message_content",
        "receiver": 1 /* Receiver user's id */
    }

Example Response::

    HTTP 201 CREATED
    {
        "id": 6,
        "title": "message_title",
        "content": "message_content",
        "sender": {
            "id": 1,
            "username": "sender_user"
        },
        "receiver": {
            "id": 3,
            "username": "receiver_user"
        },
        "is_read": false,
        "date_created": "2019-12-22T05:10:54.454827+03:00"
    }


List Received Direct Messages
-----------------

Method: **GET**

Endpoint: **/api/direct-messages/receivers/**

Example Request::

    GET /api/direct-messages/received/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 5,
            "title": "message_title",
            "content": "message_content",
            "sender": {
                "id": 4,
                "username": "sender_user"
            },
            "receiver": {
                "id": 1,
                "username": "receiver_user"
            },
            "is_read": true,
            "date_created": "2019-12-22T04:48:39.291998+03:00"
        }
    ]


List Sent Direct Messages
-----------------

Method: **GET**

Endpoint: **/api/direct-messages/receivers/**

Example Request::

    GET /api/direct-messages/sent/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 3,
            "title": "message_title",
            "content": "message_content",
            "sender": {
                "id": 1,
                "username": "sender_user"
            },
            "receiver": {
                "id": 2,
                "username": "receiver_user"
            },
            "is_read": false,
            "date_created": "2019-12-22T04:29:33.087257+03:00"
        }
    ]


Get Direct Message Detail
-----------------

Method: **GET**

Endpoint: **/api/direct-messages/<direct_message_id>/**

Example Request::

    GET /api/direct-messages/3/

Example Response::

    HTTP 200 OK
    {
        "id": 3,
        "title": "message_title",
        "content": "message_content",
        "sender": {
            "id": 1,
            "username": "sender_user"
        },
        "receiver": {
            "id": 2,
            "username": "receiver_user"
        },
        "is_read": true, /* This will be set true here. */
        "date_created": "2019-12-22T04:29:33.087257+03:00"
    }


Delete Direct Message
-----------------

Method: **GET**

Endpoint: **/api/direct-messages/<direct_message_id>/**

Example Request::

    DELETE /api/direct-messages/3/

Example Response::

    HTTP 204 NO CONTENT
