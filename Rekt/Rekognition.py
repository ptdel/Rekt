import boto3
from Config import configuration


class Rekognition:
    def __init__(self, config):
        self.rekognition = boto3.client("rekognition")
        self.checks = config.rekognition.check_types

    def run_checks(self, image):
        return list(
            map(
                lambda _: getattr(self.rekognition, _)(Image={"Bytes": image}),
                self.checks,
            )
        )


rekognition = Rekognition(configuration)
