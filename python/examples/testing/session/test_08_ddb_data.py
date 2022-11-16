WITH_DATA = {
    "Count": 10,
    "Items": [
        {"id": {"N": "187"}, "name": {"S": "Abderrezzak"}},
        {"id": {"N": "154"}, "name": {"S": "Abdennaji"}},
        {"id": {"N": "7"}, "name": {"S": "Aamar"}},
        {"id": {"N": "115"}, "name": {"S": "Abdelmonaim"}},
        {"id": {"N": "117"}, "name": {"S": "Abdelmoughit"}},
        {"id": {"N": "47"}, "name": {"S": "Abdelazis"}},
        {"id": {"N": "184"}, "name": {"S": "Abderrazzak"}},
        {"id": {"N": "156"}, "name": {"S": "Abdennaser"}},
        {"id": {"N": "122"}, "name": {"S": "Abdeloihab"}},
        {"id": {"N": "145"}, "name": {"S": "Abdenabi"}},
    ],
    "ResponseMetadata": {
        "HTTPHeaders": {
            "connection": "keep-alive",
            "content-length": "9031",
            "content-type": "application/x-amz-json-1.0",
            "date": "Tue, 15 Nov 2022 14:17:29 GMT",
            "server": "Server",
            "x-amz-crc32": "2018689941",
            "x-amzn-requestid": "K7HMQVMVCK2JM95NHQN0CGSI2FVV4KQNSO5AEMVJF66Q9ASUAAJG",
        },
        "HTTPStatusCode": 200,
        "RequestId": "K7HMQVMVCK2JM95NHQN0CGSI2FVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "RetryAttempts": 0,
    },
    "ScannedCount": 205,
}

WITHOUT_DATA = {
    "Count": 0,
    "Items": [],
    "ResponseMetadata": {
        "HTTPHeaders": {
            "connection": "keep-alive",
            "content-length": "9031",
            "content-type": "application/x-amz-json-1.0",
            "date": "Tue, 15 Nov 2022 14:17:29 GMT",
            "server": "Server",
            "x-amz-crc32": "2018689941",
            "x-amzn-requestid": "K7HMQVMVCK2JM95NHQN0CGSI2FVV4KQNSO5AEMVJF66Q9ASUAAJG",
        },
        "HTTPStatusCode": 200,
        "RequestId": "K7HMQVMVCK2JM95NHQN0CGSI2FVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "RetryAttempts": 0,
    },
    "ScannedCount": 205,
}

EXPECTED_RESULT = [
    {"id": {"N": "187"}, "name": {"S": "Abderrezzak"}},
    {"id": {"N": "154"}, "name": {"S": "Abdennaji"}},
    {"id": {"N": "7"}, "name": {"S": "Aamar"}},
    {"id": {"N": "115"}, "name": {"S": "Abdelmonaim"}},
    {"id": {"N": "117"}, "name": {"S": "Abdelmoughit"}},
    {"id": {"N": "47"}, "name": {"S": "Abdelazis"}},
    {"id": {"N": "184"}, "name": {"S": "Abderrazzak"}},
    {"id": {"N": "156"}, "name": {"S": "Abdennaser"}},
    {"id": {"N": "122"}, "name": {"S": "Abdeloihab"}},
    {"id": {"N": "145"}, "name": {"S": "Abdenabi"}},
]
