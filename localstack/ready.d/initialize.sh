#!/usr/bin/env bash

awslocal s3 mb s3://map-stock

SQS_QUEUE_URL=$(awslocal sqs create-queue --queue-name maps-uploaded | jq -r '.QueueUrl')
SQS_QUEUE_ARN=$(awslocal sqs get-queue-attributes --attribute-names QueueArn --queue-url $SQS_QUEUE_URL | jq -r '.Attributes.QueueArn')

awslocal s3api put-bucket-notification-configuration \
    --bucket map-stock \
    --notification-configuration '{
        "QueueConfigurations": [
            {
                "Id": "MyS3EventNotification",
                "Events": ["s3:ObjectCreated:*"],
                "QueueArn": "'$SQS_QUEUE_ARN'"
            }
        ]
    }'
