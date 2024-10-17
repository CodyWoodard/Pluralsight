FROM python

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/app.py .

CMD ["python", "./app.py"]