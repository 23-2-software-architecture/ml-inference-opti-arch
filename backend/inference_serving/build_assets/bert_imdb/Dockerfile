FROM swarch-23-2-ml-docker-base

WORKDIR /app

COPY ./models/bert_imdb /app/bert_imdb

COPY ./build_assets/bert_imdb/main.py /app

EXPOSE 8501

CMD ["uvicorn", "main:app", "--port", "8080", "--host", "0.0.0.0"]

