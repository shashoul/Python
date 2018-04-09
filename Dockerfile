FROM python:3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY citytemp.py .
CMD ["python3","citytemp.py"]
