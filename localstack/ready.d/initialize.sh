#!/usr/bin/env bash

awslocal sqs create-queue \
    --queue-name maps-uploaded

awslocal dynamodb create-table \
    --table-name users \
    --billing-mode PAY_PER_REQUEST \
    --attribute-definitions \
        AttributeName=username,AttributeType=S \
    --key-schema \
        AttributeName=username,KeyType=HASH

awslocal dynamodb create-table \
    --table-name maps \
    --billing-mode PAY_PER_REQUEST \
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH
