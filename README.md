# Scraper for trust-pilot

## Introduction
This project is built to scrape review data from trust pilot and expose a
FastAPI endpoint to fetch the data.

## Installation

**MacOS**

Requirements:

- Python 3.9+

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

## Versioning

| Version     |                            Description        |
| ----------- | ----------------------------------------------|
|0.0.1        | This version scrapes data from a given website|


## API docs

Check the FastAPI docs at [0.0.0.0:80/docs]
