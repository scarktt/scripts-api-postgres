FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPYCACHEPREFIX=/tmp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . ./

CMD gunicorn --workers 4 --bind :$API_PORT --timeout 0 src.main:app --reload
