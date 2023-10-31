# Scraper for trust-pilot

## Introduction
This project is built to scrape review data from trust pilot and expose a
FastAPI endpoint to fetch the data.

## Version

| Version     |                            Description        |
| ----------- | ----------------------------------------------|
|0.0.1        | This version scrapes data from a given website|

## Installation

Requirements:

- Python 3.9+
- Docker

**MacOS**

Setup:

1. Clone the repository
```{bash}
$ git clone https://github.com/storymachinedata/trustpilot_scraper.git # https
or
$ git clone git@github.com:storymachinedata/trustpilot_scraper.git # ssh
```

2. Initialize the virtualEnv
```{bash}
$ cd trustpilot_scraper
$ pip install virtualenv
$ python3 -m venv .env
```

3. Activate the environment
```{bash}
$ source .env/bin/activate
```

4. Install required libraries
```{bash}
$ pip install --no-cache-dir -r requirements.txt
```

**Windows**

1. Clone the repository
```{bash}
$ git clone https://github.com/storymachinedata/trustpilot_scraper.git # https
or
$ git clone git@github.com:storymachinedata/trustpilot_scraper.git # ssh
```

2. Initialize the virtualEnv
```{bash}
$ cd trustpilot_scraper
$ pip install virtualenv
$ python3 -m venv .env
```

3. Activate the environment
```{bash}
$ .\.env\Scripts\activate
```

4. Install required libraries
```{bash}
$ pip install --no-cache-dir -r requirements.txt
```
## Running the API

1. Build Docker image
```{bash}
$ docker build -t trust-pilot-scraper:0.0.1 .
```

2. Run Docker container
```{bash}
$ docker run -p 80:80 trust-pilot-scraper:0.0.1
```
visit the url [0.0.0.0:80/docs](http://0.0.0.0:80/docs)

## API documentation

Check the FastAPI docs at [0.0.0.0:80/docs](http://0.0.0.0:80/docs)