FROM python:3.11.6

WORKDIR /app

COPY ./build_assets/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./build_assets/main.py /app/

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]