import logging.config

from utilities import tesseract, functions

logger = logging.getLogger(__name__)


def process_event(event_type, event):
    logger.info(f"Event type: {event_type} | Event src_path: {event.src_path}")
    excel_path = functions.validate_path(event.src_path)
    if not functions.verify(source_path=excel_path):
        logger.error(f"File path '{excel_path}' is not valid!")
    pdf_path = functions.get_pdf_path(excel_path=excel_path)
    if not pdf_path.exists():
        logger.error(f"PDF path '{pdf_path}' does not exist!")
        return
    tesseract.process(pdf_path=pdf_path, excel_path=excel_path)
