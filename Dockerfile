FROM python:3.11

ENV PYTHONDONTWRITEBYTECOD=1
ENV PYTHONUNBUFFERED=1


WORKDIR /feedback_app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /feedback_app


CMD ["gunicorn", "--bind", "0.0.0.0:8080", "DDS_feedback.wsgi"]