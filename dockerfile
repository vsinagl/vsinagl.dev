FROM python:3.10.15-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV port=8080

COPY . .


CMD [ "python3", "./src/app.py" ]
