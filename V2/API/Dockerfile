FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./dummy_app.py /code/app.py

EXPOSE 8000

CMD ["fastapi", "run", "app.py", "--port", "8000"]