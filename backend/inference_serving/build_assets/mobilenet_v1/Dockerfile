FROM swarch-23-2-ml-docker-base

WORKDIR /app

COPY ./models/mobilenet_v1 /app/mobilenet_v1

COPY ./build_assets/mobilenet_v1/main.py /app

EXPOSE 8501

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

