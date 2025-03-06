FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
  PYTHONPYCACHEPREFIX=/tmp \
  PYTHONPATH=/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY requirements_dev.txt .
RUN pip install -r requirements_dev.txt

COPY . ./

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
