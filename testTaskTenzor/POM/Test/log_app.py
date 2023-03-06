from loguru import logger


def log_open():
    logger.add('file_log.log', format='{time} {level} {message}',
               level='INFO', rotation='10:00', compression='zip')


