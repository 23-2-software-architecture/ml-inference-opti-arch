FROM swarch-23-2-ml-preprocess-docker-base

WORKDIR /app

COPY ./models/mobilenet_v1 /app/mobilenet_v1

COPY ./build_assets/mobilenet_v1/main.py /app

COPY ./build_assets/mobilenet_v1/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

