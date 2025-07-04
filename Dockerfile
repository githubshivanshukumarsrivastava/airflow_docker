FROM apache/airflow:2.9.0

COPY requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt
