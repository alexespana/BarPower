import pytest, os
from bar_power.config import Config

@pytest.fixture
def config():
    config = Config()
    return config

def test_correct_log_dir(config):
    if(os.getenv('LOG_DIR')):
        assert config.get_log_directory() == os.getenv('LOG_DIR')
    else:
        assert config.get_log_directory() == '/tmp/barpower/log/'

def test_correct_log_file(config):
    if(os.getenv('LOG_FILE')):
        assert config.get_log_file() == os.getenv('LOG_FILE')
    else:
        assert config.get_log_file() == 'bar_power.log'
