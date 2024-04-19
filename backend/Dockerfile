FROM python
COPY requierments.txt /worky/
WORKDIR /worky
RUN pip install --no-cache-dir -r requierments.txt 
COPY . .

CMD python app.py