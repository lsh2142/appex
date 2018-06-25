import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle(event, context):
    logger.info("%s - %s",event, context)
    return event
