FROM python:3.9

WORKDIR /app

COPY app.py .

RUN pip install flask prometheus_client

EXPOSE 8000 5000

CMD ["python", "app.py"]
