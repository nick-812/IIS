FROM python:3

RUN pip install tk
RUN pip install requests
RUN pip install pytest
RUN pip install pandas


COPY src/client/weatherapp.py .
COPY data/processed/obdelani.csv .

CMD export DISPLAY=127.0.0.1:0.0
CMD ["python", "./weatherapp.py"]