FROM python:3

RUN pip install fastapi
RUN pip install numpy
RUN pip install uvicorn
RUN pip install pydantic
RUN pip install keras
RUN pip install typing
RUN pip install requests
RUN pip install pytest
RUN pip install pandas
RUN pip install -U scikit-learn scipy matplotlib


EXPOSE 8085

COPY src/serve/server.py .
COPY models/model.pkl .

CMD ["python", "./server.py"]