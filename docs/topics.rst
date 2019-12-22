Create Topic
-----------------

Method: **POST**

Endpoint: **/api/topics/**

Example Request::

    POST /api/topics/
    {
        "title": "topic_title"
    }

Example Response::

    HTTP 201 CREATED
    {
        "id": 9,
        "title": "topic_title",
        "user": {
            "id": 1,
            "username": "my_username"
        },
        "entries": [],
        "date_created": "2019-12-21T23:27:17.895665+03:00",
        "date_updated": "2019-12-21T23:27:17.897780+03:00"
    }


Get Topics
-----------------

Method: **GET**

Endpoint: **/api/topics/**

Query parameters:

- ``keywords`` (optional, comma separated strings): To list topics whose title includes the given keywords.

Example Request::

    GET /api/topics/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 1,
            "title": "topic_title1",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "entries": [
                {
                    "id": 1,
                    "content": "entry_content1",
                    "user": {
                        "id": 1,
                        "username": "my_username"
                    },
                    "date_created": "2019-12-21T22:30:52.638672+03:00",
                    "date_updated": "2019-12-21T23:15:07.427046+03:00"
                },
                {
                    "id": 2,
                    "content": "entry_content2",
                    "user": {
                        "id": 2,
                        "username": "my_username"
                    },
                    "date_created": "2019-12-21T22:30:52.638672+03:00",
                    "date_updated": "2019-12-21T23:15:07.427046+03:00"
                }
            ],
            "date_created": "2019-12-21T19:09:27.878108+03:00",
            "date_updated": "2019-12-21T19:09:27.880234+03:00"
        },
        {
            "id": 2,
            "title": "topic_title2",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "entries": [
                {
                    "id": 3,
                    "content": "entry_content3",
                    "user": {
                        "id": 3,
                        "username": "my_username"
                    },
                    "date_created": "2019-12-21T22:30:52.638672+03:00",
                    "date_updated": "2019-12-21T23:15:07.427046+03:00"
                }
            ],
            "date_created": "2019-12-21T19:09:27.878108+03:00",
            "date_updated": "2019-12-21T19:09:27.880234+03:00"
        },
    ]


Get Topic Detail
-----------------

Method: **GET**

Endpoint: **/api/topics/<topic_id>/**

Example Request::

    GET /api/topics/9/

Example Response::

    HTTP 200 OK
    {
        "id": 9,
        "title": "topic_title",
        "user": {
            "id": 3,
            "username": "my_username"
        },
        "entries": [],
        "date_created": "2019-12-21T23:27:17.895665+03:00",
        "date_updated": "2019-12-21T23:27:17.897780+03:00"
    }


Update Topic
-----------------

Method: **PATCH**

Endpoint: **/api/topics/<topic_id>/**

Example Request::

    PATCH /api/topics/9/
    {
        "title": "edited_topic_title"
    }

Example Response::

    HTTP 200 OK
    {
        "id": 9,
        "title": "edited_topic_title",
        "user": {
            "id": 3,
            "username": "my_username"
        },
        "entries": [],
        "date_created": "2019-12-21T23:27:17.895665+03:00",
        "date_updated": "2019-12-21T23:34:36.403716+03:00"
    }


Delete Topic
-----------------

Method: **DELETE**

Endpoint: **/api/topics/<topic_id>/**

Example Request::

    DELETE /api/topics/9/

Example Response::

    HTTP 204 NO CONTENT


List Topic Entries
-----------------

Method: **GET**

Endpoint: **/api/topics/<topic_id>/entries/**

Query parameters:

- ``keywords`` (optional, comma separated strings): To list entries whose content includes the given keywords.

Example Request::

    GET /api/topics/9/entries/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 1,
            "content": "entry_content1",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "date_created": "2019-12-21T22:29:17.561338+03:00",
            "date_updated": "2019-12-21T22:29:17.562295+03:00"
        },
        {
            "id": 2,
            "content": "entry_content2",
            "user": {
                "id": 2,
                "username": "my_username"
            },
            "date_created": "2019-12-21T22:30:52.638672+03:00",
            "date_updated": "2019-12-21T23:15:07.427046+03:00"
        },
        {
            "id": 3,
            "content": "entry_content3",
            "user": {
                "id": 3,
                "username": "my_username"
            },
            "date_created": "2019-12-21T23:40:00.202038+03:00",
            "date_updated": "2019-12-21T23:40:00.203040+03:00"
        }
    ]


Create Topic Entry
-----------------

Method: **POST**

Endpoint: **/api/topics/<topic_id>/entries/**

Example Request::

    POST /api/topics/9/entries/
    {
        "content": "entry_content1"
    }

Example Response::

    HTTP 201 CREATED
    {
        "id": 7,
        "content": "entry_content",
        "user": {
            "id": 1,
            "username": "my_username"
        },
        "date_created": "2019-12-21T23:42:26.678723+03:00",
        "date_updated": "2019-12-21T23:42:26.680176+03:00"
    }


List Entries
-----------------

Method: **GET**

Endpoint: **/api/entries/**

Query parameters:

- ``keywords`` (optional, comma separated strings): To list entries whose content includes the given keywords.

Example Request::

    GET /api/topics/9/entries/

Example Response::

    HTTP 200 OK
    [
        {
            "id": 1,
            "content": "entry_content1",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "topic": {
                "id": 1,
                "title": "topic_title1",
                "user": 1,
                "date_created": "2019-12-21T19:09:27.878108+03:00",
                "date_updated": "2019-12-21T19:09:27.880234+03:00"
            },
            "date_created": "2019-12-21T22:29:17.561338+03:00",
            "date_updated": "2019-12-21T22:29:17.562295+03:00"
        },
        {
            "id": 2,
            "content": "entry_content2",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "topic": {
                "id": 2,
                "title": "topic_title2",
                "user": 2,
                "date_created": "2019-12-21T19:09:27.878108+03:00",
                "date_updated": "2019-12-21T19:09:27.880234+03:00"
            },
            "date_created": "2019-12-21T22:30:52.638672+03:00",
            "date_updated": "2019-12-21T23:15:07.427046+03:00"
        },
        {
            "id": 3,
            "content": "entry_content3",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "topic": {
                "id": 3,
                "title": "topic_title3",
                "user": 3,
                "date_created": "2019-12-21T19:09:27.878108+03:00",
                "date_updated": "2019-12-21T19:09:27.880234+03:00"
            },
            "date_created": "2019-12-21T23:40:00.202038+03:00",
            "date_updated": "2019-12-21T23:40:00.203040+03:00"
        },
        {
            "id": 4,
            "content": "entry_content4",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "topic": {
                "id": 4,
                "title": "topic_title4",
                "user": 1,
                "date_created": "2019-12-21T19:09:27.878108+03:00",
                "date_updated": "2019-12-21T19:09:27.880234+03:00"
            },
            "date_created": "2019-12-21T23:42:26.678723+03:00",
            "date_updated": "2019-12-21T23:42:26.680176+03:00"
        }
    ]


Get Entry Detail
-----------------

Method: **GET**

Endpoint: **/api/entries/<entry_id>/**

Example Request::

    GET /api/entries/4/

Example Response::

    HTTP 200 OK
    {
        "id": 4,
        "content": "entry_content",
        "user": {
            "id": 1,
            "username": "my_username"
        },
        "topic": {
            "id": 4,
            "title": "topic_title",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "date_created": "2019-12-21T19:09:27.878108+03:00",
            "date_updated": "2019-12-21T19:09:27.880234+03:00"
        },
        "date_created": "2019-12-21T22:29:17.561338+03:00",
        "date_updated": "2019-12-21T22:29:17.562295+03:00"
    }


Update Entry
-----------------

Method: **PATCH**

Endpoint: **/api/entries/<entry_id>/**

Example Request::

    PATCH /api/entries/4/
    {
        "content": "edited_entry_content"
    }

Example Response::

    HTTP 200 OK
    {
        "id": 4,
        "content": "edited_entry_content",
        "user": {
            "id": 1,
            "username": "my_username"
        },
        "topic": {
            "id": 4,
            "title": "topic_title",
            "user": {
                "id": 1,
                "username": "my_username"
            },
            "date_created": "2019-12-21T19:09:27.878108+03:00",
            "date_updated": "2019-12-21T19:09:27.880234+03:00"
        },
        "date_created": "2019-12-21T22:29:17.561338+03:00",
        "date_updated": "2019-12-21T23:49:24.220481+03:00"
    }


Delete Entry
-----------------

Method: **DELETE**

Endpoint: **/api/entries/<entry_id>/**

Example Request::

    DELETE /api/entries/4/

Example Response::

    HTTP 204 NO CONTENT
