#!/usr/bin/env bash

awslocal sqs create-queue \
    --queue-name maps-uploaded

awslocal dynamodb create-table \
    --table-name users \
    --billing-mode PAY_PER_REQUEST
    --key-schema AttributeName=username,KeyType=HASH \
    --attribute-definitions AttributeName=username,AttributeType=S

awslocal dynamodb create-table \
    --table-name maps \
    --billing-mode PAY_PER_REQUEST
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S
