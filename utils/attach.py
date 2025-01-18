import json
import logging

import allure
from allure_commons.types import AttachmentType
from requests import Response


def response_attaching(response: Response):
    allure.attach(
        body=response.request.method,
        name="Request method",
        attachment_type=AttachmentType.TEXT,
    )

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

    if response.content != b'':
        if response.json():
            allure.attach(
                body=json.dumps(response.json(), indent=4, ensure_ascii=True),
                name="Response",
                attachment_type=AttachmentType.JSON,
                extension="json",
            )


def response_logging(response: Response):
    logging.info("Request: " + response.request.method + ' ' + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)  # логирование тела запроса если оно есть
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)
