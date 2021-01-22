# 3-onbuild will install dependencies in requirements.txt automatically
FROM python:3-onbuild

# 3-onbuild expects path 'usr/src'
COPY . /usr/src/app

CMD ["python", "api.py"]
