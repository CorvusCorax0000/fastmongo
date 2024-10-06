FROM python:3.10

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/CorvusCorax0000/fastmongo.git /app

WORKDIR /app/python-app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
