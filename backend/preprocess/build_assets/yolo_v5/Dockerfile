FROM swarch-23-2-ml-preprocess-docker-base

WORKDIR /app

RUN apt update && \
    apt -y install libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

COPY ./build_assets/yolo_v5/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./build_assets/yolo_v5/main.py /app

EXPOSE 8080

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

