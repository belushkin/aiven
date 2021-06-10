# aiven

## How to build and run application
### Build base image
docker build -f Dockerfile -t aiven .

### Build producer image and run
docker build -f Dockerfile.producer -t aiven_producer . && docker run --env-file .env -it aiven_producer

### Build consumer image and run
docker build -f Dockerfile.consumer -t aiven_consumer . && docker run --env-file .env -it aiven_consumer

