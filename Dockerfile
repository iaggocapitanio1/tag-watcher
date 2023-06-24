FROM python:3.10.12-slim-buster


RUN apt-get update && apt-get -y install libpq-dev gcc apt-transport-https && pip install --upgrade pip  \
    && mkdir -pv /var/{log,run}/gunicorn/ && mkdir -pv /home/app \
    && apt-get update && apt-get -y install tesseract-ocr && apt-get update && apt-get install -y libgl1-mesa-glx  \
    && apt-get install -y poppler-utils

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    APP_DIR=/home/app\
    WHATCH_DIR=/home/app/media/public/mofreitas/clientes

WORKDIR $APP_DIR

COPY . $APP_DIR/
COPY requirements.txt $APP_DIR/requirements.txt

RUN chmod +x $APP_DIR/requirements.txt && mkdir -pv $WHATCH_DIR

RUN python3 -m pip install -r requirements.txt

COPY main.py .

CMD [ "python", "./main.py" ]