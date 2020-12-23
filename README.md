# Hyperledger-Sawtooth-Tutorial

## Usage

Start the pre-built Docker containers in development mode:
```bash
docker-compose -f docker-compose-devmod.yaml up
```

or, the pre-built Docker containers in production mode:
```bash
docker-compose -f docker-compose-promod.yaml up
```

At this point all the containers should be running.

To launch the DApp, you could do this:
```bash
docker exec -it iot-dapp bash
```

Sample command usage:

```bash
cd dapp
./iot_dapp # To execute dapp

# Client DApp Menu
1 - store sensor data
2 - get sensor data
3 - get sensor history
4 - exit
```

Finalize docker containers
```bash
docker-compose -f docker-compose-devmod.yaml down -v
```
or
```bash
docker-compose -f docker-compose-promod.yaml down -v
```