FROM python:3.9
WORKDIR /app
ADD . /app
COPY requirements.txt /app
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install ibm_db
RUN python3 -m pip install requests
EXPOSE 5000
CMD ["python", "app.py"]