FROM python:3.9

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home/app_user

ENV PYTHONPATH=/home/app_user

COPY . ./

RUN python3 -m pip install --upgrade pip setuptools
RUN python3 -m pip install --no-cache-dir -r requirements.txt

USER app_user

CMD ["bash"]