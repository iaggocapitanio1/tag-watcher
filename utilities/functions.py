import logging
import re
from pathlib import Path
from typing import Union
import settings

logger = logging.getLogger(__name__)


def clean_name(name: str) -> str:
    return re.sub(r'[^\w]', '_', name)


def validate_path(path: Union[str, Path]) -> Path:
    if isinstance(path, str):
        path = Path(path)
    return path.resolve()


def get_pdf_path(excel_path: Path) -> Path:
    pdf_name = excel_path.stem + "_ETQs.pdf"
    return excel_path.with_name(pdf_name)


def verify(source_path: Path) -> bool:
    """
    Verifies if the given source path contains the specified reference as one of its parts and
    if it is not a directory.

    This function takes a path and a reference string as input. It first checks if the source_path
    is a directory, and if so, returns False. It then checks if the reference string is part of the path.
    If it is, the function traverses up the path to confirm if any part of the path matches the reference string.

    :param source_path: A Path object representing the source path to be verified.
    :return: True if the source path contains the reference and is not a directory, False otherwise.
    """
    if source_path.is_dir():
        return False
    if settings.CUT_LIST_DIR not in source_path.parts:
        return False
    current_path = Path(*source_path.parts[source_path.parts.index(settings.CUT_LIST_DIR):])
    while current_path != current_path.parent:  # Stop when reaching the root directory
        if current_path.name == settings.CUT_LIST_DIR:
            return True
        current_path = current_path.parent
    return False
