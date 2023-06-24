from pathlib import Path
from dotenv import load_dotenv
import os


def str_to_bool(target) -> bool:
    if isinstance(target, bool):
        return target
    return target.lower() == 'true'


def mega_bytes_to_bits(mega: int) -> int:
    return mega * 1024 * 1024


BASE_DIR = Path(__file__).resolve().parent

PRODUCTION = True

if not PRODUCTION:
    load_dotenv(BASE_DIR.joinpath('.dev.env'))
else:
    load_dotenv()

NAMESPACE = 'TAG_WATCHER'

if NAMESPACE:
    NAMESPACE += '_'


def parse_env(string: str) -> str:
    return NAMESPACE + string


DELAY_FOR_SCAN = int(os.environ.get(parse_env("DELAY_FOR_SCAN"), 5))

MAPPING_FILE = os.environ.get(parse_env("MAPPING_FILE"), "MAPPING.xlsx")

SLEEP_DURATION = int(os.environ.get(parse_env("DELAY_FOR_SCAN"), 1))

NUM_WORKER_THREADS = int(os.environ.get(parse_env("NUM_WORKER_THREADS"), 4))

PATH_REFERENCE = os.environ.get(parse_env("PATH_REFERENCE"), "mofreitas/clientes/")

WATCHING_DIR = os.environ.get(parse_env("WATCHING_DIR"), BASE_DIR / '/home/app/media/public/mofreitas')

WATCHING_DIR = Path(WATCHING_DIR).resolve()

CUT_LIST_DIR = "Listas de Corte e Etiquetas"

KEYWORD = "clientes"

LOG_DIR = BASE_DIR.joinpath('logs')

LOG_DIR.mkdir(exist_ok=True, parents=True)

LOGGER = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - level: %(levelname)s - loc: %(name)s - func: %(funcName)s - msg: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR.joinpath('tag-watcher.log'),
            "level": "DEBUG",
            "maxBytes": mega_bytes_to_bits(mega=1),
            "backupCount": 3,
            "formatter": "simple"
        }
    },
    "loggers": {
        "utilities": {
            "level": "DEBUG",
            "handlers": [
                "console",
                "file"
            ],
            "propagate": True
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file"
        ],
    }
}
