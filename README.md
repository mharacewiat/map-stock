Map Stock
=

# Description

This project is a solution to the [challenge](MapStock-challenge.pdf). 

# Installation

Execute the command from bellow. It will spin up the localstack resources and run the Flask app under `http://127.0.0.1:5000/`.

```shell
docker compose up -d --build
```

# Usage

## Create a user

First, there has to be at least one user existing in the database. To create one execute the command from below.

```shell
docker compose exec app flask user foo bar 1 # <username> <password> <is_active>
```

> Use the same command to modify the user. You might want to "toggle" the `is_active` flag.

## Issue a access token

With the credentials from previous step, issue a new access token:

```shell
curl --location 'http://127.0.0.1:5000/api/v1/auth' \
    --header 'Content-Type: application/json' \
    --data '{
        "username": "foo",
        "password": "bar"
    }'
```

## Upload a file

Take the `access_token` from the previous response and use it in `Authorization` header for future requests.

```shell
curl --location 'http://127.0.0.1:5000/api/v1/maps' \
    --header 'Authorization: Bearer <access_tolen>' \
    --form 'file=@"/path/to/my/file.txt"'
```

> In the response you'll receive an uuid, that could be shared with other users.

## Process the map

After map was uploaded, it's not available to download. System sent a message to the queue. The message is supposed to be picked up by an external system. For testing purposes there's a utility tool available that "processes" a one message at a time.

```shell
docker compose exec app flask queue
```

> The step is optional. It's recomended to skip it before testing if file can be downloaded before being processed.

## Download the map

```shell
curl --location 'http://127.0.0.1:5000/api/v1/maps/<id>' \
    --header 'Authorization: Bearer <access_tolen>'
```

> This endpoint is also available for guests. To act as a guest, simply remove `Authorization` header.

# Testing

```shell
docker compose exec app python -m unittest discover
```

# Summary

- The cli commands (and MessageGateway.read) were written in hurry. I didn't pay attention to tests and their placement. I'd put them in a separate folders eventually.
- I didn't make it on time to write functional tests. I focused on green-path tests only. There's also one test that that I couldn't resolve (I skipped it).
- I entered an endless rabbit hole trying many things and trying to deliver a working application. I'm sure this solution would be cleaner if I have had spent another week here.
- I decided to use Flask, as this is the first framework I'm learning with Python. I learned and practiced a lot, but there are still things uncertain to me.
- I decided to implement rough security layer. Ideally that would be a separate container acting as OAuth authorization server.
- I didn't make it on time writing OpenApi/Swagger specs. They would be of course delivered in a regular project.
- The error handling is awful. That would be a next thing to do. I know Flask allows to write a custom error handler.
- I've decided to use NoSQL database, because instructions were not suggesting any requirement for relations. If there was a requirement for map editing (only by the user who uploaded it), or a user-scoped sharing... then maybe a relational db would a better choice.

# Future Idea

For a production scale I'd favor a serverless, little-to-none code approach. This would help scaling the app and not worry about the infrastructure too much.

The idea I have in mind is adding to the stack: S3 with CloudFront, API Gateway, Cognito User Pools and Lambdas/ECS.

- Uploading files would be done against S3 faced by API Gateway (multipart). SQS would receive notification without the need to write any code.
- Authorization delegated to Cognito and integrated with API Gateway (with custom authenticator lambda)
- Lambda or ECS task (for longer processing) to pick up the message from the queue and process it. Update DynamoDB table row.
- Lambda to get the file, or rather a signed url to S3 with the processed file.
