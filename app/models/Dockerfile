FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV CONFIGURATION_FILE_PATH=/etc/telegraf/python_fastapi/telegraf.conf

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]