FROM swarch-23-2-ml-docker-base

WORKDIR /app

COPY ./models/yolo_v5 /app/yolo_v5

COPY ./build_assets/yolo_v5/main.py /app

EXPOSE 8501

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

