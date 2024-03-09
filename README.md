Map Stock
=

# Description

This project is a solution to the [challenge](MapStock-challenge.pdf).

# Installation

```shell
docker compose build
```

# Usage

Execute the command from bellow and visit `http://localhost:80`.

```shell
docker compose up -d
```

# Testing

```shell
docker compose exec -it app python -m unittest discover
```
