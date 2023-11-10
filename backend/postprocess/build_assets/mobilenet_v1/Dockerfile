FROM swarch-23-2-ml-postprocess-docker-base

WORKDIR /app

COPY ./build_assets/mobilenet_v1/imagenet_labels.pkl /app

COPY ./build_assets/mobilenet_v1/main.py /app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

