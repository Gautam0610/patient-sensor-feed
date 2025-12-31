# Patient Sensor Feed

This project simulates patient sensor data and sends it to Kafka. It consists of two main components:

*   **producer**: Generates synthetic patient vital signs data and publishes it to a Kafka topic.
*   **app**: A consumer application that subscribes to the Kafka topic and processes the data.

## Usage

1.  **Prerequisites**
    *   Docker
    *   Docker Compose (Optional)
    *   Kafka cluster

2.  **Configuration**
    *   Configure the Kafka broker address in both `producer/producer.py` and `app/consumer.py`.

3.  **Running the Producer**
    ```bash
    cd producer
    # Build the Docker image
    docker build -t producer .
    # Run the Docker container
    docker run producer
    ```

4.  **Running the Consumer**
    ```bash
    cd app
    # Build the Docker image
    docker build -t consumer .
    # Run the Docker container
    docker run consumer
    ```

## Docker Compose (Optional)

You can use Docker Compose to orchestrate the producer and consumer applications.

1.  Create a `docker-compose.yml` file in the root directory of the project.

    ```yaml
    version: "3.9"
    services:
      producer:
        build: ./producer
        depends_on:
          - kafka
        environment:
          KAFKA_BROKER: <kafka_broker_address>

      consumer:
        build: ./app
        depends_on:
          - kafka
        environment:
          KAFKA_BROKER: <kafka_broker_address>

      kafka:
        image: docker.io/bitnami/kafka:latest
        ports:
          - "9092:9092"
        environment:
          KAFKA_CFG_NODE_ID: 0
          KAFKA_CFG_PROCESS_ROLES: "controller,broker"
          KAFKA_CFG_LISTENERS: "PLAINTEXT://:9092,CONTROLLER://:9093"
          KAFKA_CFG_ADVERTISED_LISTENERS: "PLAINTEXT://localhost:9092"
          KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: "0@kafka:9093"
          KAFKA_CFG_CONTROLLER_LISTENER_NAMES: "CONTROLLER"
    ```

2.  Run Docker Compose:

    ```bash
    docker-compose up -d
    ```