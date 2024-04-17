FROM python
COPY requirements.txt /worky/
WORKDIR /worky
RUN pip install -r requirements.txt 
COPY . .

CMD python auth.py