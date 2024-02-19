FROM python:3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY Backend/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "arch_backend/manage.py", "runserver", "0.0.0.0:8000"]
