FROM python:3.10
EXPOSE 5000
WORKDIR /app

RUN pip3 install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel

COPY requirements.txt .
RUN pip install -e .
CMD ["flask", "run", "--host", "0.0.0.0"]