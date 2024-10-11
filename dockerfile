FROM python:3.10.15-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=src/app.py
ENV FLASK_ENV=production
ENV PORT=8000

EXPOSE 8000

CMD ["python3", "src/app.py"]
