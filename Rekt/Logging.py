import logging
from Config import configuration


#: the main logging object, should be used in most cases.
logging.basicConfig(
    filename=configuration.logs.logfile,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    level=logging.DEBUG,
    filemode="w",
)

console_log = logging.StreamHandler()
console_log.setLevel(logging.INFO)

logging.getLogger().addHandler(console_log)
