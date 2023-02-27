FROM python:3.10

RUN mkdir -p /app

# Install dependencies from requirements file
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
