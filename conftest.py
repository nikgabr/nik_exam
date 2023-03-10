from datetime import datetime
import logging

log = logging.getLogger(__name__)
log_path = "~/PycharmProjects/pythonProject/logs/"
screenshot_path = "~/PycharmProjects/pythonProject/screenshots/"

def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        config.option.log_file = log_path + 'log.' + timestamp