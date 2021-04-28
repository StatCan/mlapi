FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8888"]
