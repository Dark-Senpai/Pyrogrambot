# bash is easy , html is good . The same way python is easy , libraries are good 😂😀
FROM artemisfowl004/vid-compress
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","SmartBot"]
