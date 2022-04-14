# buses-back

> Backend api using DRF

# Modules
- Drivers
- Passengers
- Travels
- Buses
- Schedules

# Prerequisites

- [Docker Desktop 4.6.1](https://www.docker.com/products/docker-desktop/) (includes docker && docker-compose)

# Build Setup

In the project directory, to run docker follow the next steps

```sh
docker-compose up
```

The app runs in [http://localhost:8000](http://localhost:8000).

# Features

Base API ROUTES  [http://localhost:8000/api/](http://localhost:8000/api/) 

- CRUD: Drivers, Buses, Travels, Schedules and Passengers.
- Filter all buses on a travel with more than N% of their capacity sold.
- List the travels along with their average number of passengers.
- Default sqlite3 include in this project.
