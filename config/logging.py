import logging

logger = logging.getLogger('Logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('project_log.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s [%(filename)s]', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
