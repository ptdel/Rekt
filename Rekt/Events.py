from Config import configuration


#: image filename suffixes to check for
imgs = tuple(configuration.rekognition.image_types)

#: document filename suffixes to check for
docs = tuple(configuration.rekognition.file_types)


def hasAttachments(message):
    """ returns true if the message has an attachment """
    return hasattr(message, "attachments")


def hasImages(message):
    """ returns true if any of the message attachments are an image file """
    return any(a.filename.endswith(imgs) for a in message.attachments)


def hasDocuments(message):
    """ returns true if any of the message attachments are documents """
    return any(a.filename.endswith(docs) for a in message.attachments)


#: Checks that will be applied to each incoming message
checks = [hasAttachments, hasDocuments, hasImages]


class CheckedMessage:
    def __init__(self, message, checks=checks):
        self.message = message
        self.checks = checks

    def __call__(self):
        return {chk.__name__: chk(self.message) for chk in self.checks}
