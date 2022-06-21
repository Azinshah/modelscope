import os
from pathlib import Path

# Cache location
DEFAULT_CACHE_HOME = '~/.cache'
CACHE_HOME = os.getenv('CACHE_HOME', DEFAULT_CACHE_HOME)
DEFAULT_MS_CACHE_HOME = os.path.join(CACHE_HOME, 'modelscope/hub')
MS_CACHE_HOME = os.path.expanduser(
    os.getenv('MS_CACHE_HOME', DEFAULT_MS_CACHE_HOME))

DEFAULT_MS_DATASETS_CACHE = os.path.join(MS_CACHE_HOME, 'datasets')
MS_DATASETS_CACHE = Path(
    os.getenv('MS_DATASETS_CACHE', DEFAULT_MS_DATASETS_CACHE))

DOWNLOADED_DATASETS_DIR = 'downloads'
DEFAULT_DOWNLOADED_DATASETS_PATH = os.path.join(MS_DATASETS_CACHE,
                                                DOWNLOADED_DATASETS_DIR)
DOWNLOADED_DATASETS_PATH = Path(
    os.getenv('DOWNLOADED_DATASETS_PATH', DEFAULT_DOWNLOADED_DATASETS_PATH))

MS_HUB_ENDPOINT = os.environ.get('MS_HUB_ENDPOINT',
                                 'http://101.201.119.157:31752')
