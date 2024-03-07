Map Stock
=

# Installation

```shell
docker build -t map-stock .
```

# Usage

Execute the command from bellow and visit `http://localhost:80`.

```shell
docker run -d -p 80:5000 map-stock
```

# Development

Follow the same instructions from [Usage](#usage) section, but invoke the `app.py` manually.

```shell
docker run -it --rm -v $(pwd):/app -p 80:5000 map-stock python app.py
```

# Testing

```shell
docker run -d -p 80:5000 map-stock python -m unittest
```
