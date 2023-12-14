FROM python:alpine
LABEL authors="lepro"

WORKDIR /app

COPY . .

RUN pip3 install --upgrade setuptools --no-cache
RUN pip3 install -r requierements.txt

CMD ["python", "main.py"]
