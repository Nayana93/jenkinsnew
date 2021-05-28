FROM python:3

WORKDIR /usr/src/app

COPY manage.py ./
COPY requirments.txt ./

RUN pip install -r requirments.txt

COPY . .

EXPOSE 4000

ENTRYPOINT ["python", "./manage.py"]

CMD ["runserver", "0.0.0.0:4000"]