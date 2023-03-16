FROM python:3

RUN pip install tkinter
RUN pip install requests
RUN pip install pytest
RUN pip install pandas


COPY src/client/weatherapp.py .
COPY data/processed/obdelani.csv .

CMD ["python", "./weatherapp.py"]