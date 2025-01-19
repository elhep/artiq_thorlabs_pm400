# Base Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

COPY . .

RUN pip install .

RUN apt-get update
RUN apt-get install -y libusb-1.0-0-dev


ENV PYTHONUNBUFFERED=1
CMD ["python", "artiq_thorlabs_pm400/aqctl_artiq_thorlabs_pm400.py", "--simulation"]
#CMD ["pytest", "artiq_thorlabs_pm400/test_artiq_thorlabs_pm400.py"]
