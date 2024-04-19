FROM python
COPY requirements.txt /worky/
WORKDIR /worky
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .

CMD python auth.py