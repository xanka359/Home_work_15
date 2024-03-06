import json
import allure
from allure import attachment_type


def test_attachments():
    allure.attach("Hello!", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Nice to see you there!</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(json.dumps("Are you all right?"), name="Json", attachment_type=attachment_type.JSON)
