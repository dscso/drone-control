# drone-control

To start the program just run:

```bash
docker-compose up
```

The drone should take off and start moving.

Otherwise if you just want to test the program without running the program you can also run the following command to test the connection with the drone:

```bash
docker-compose up -d
sleep 10 # wait till eveything is up and running
docker exec -it controller /bin/bash -c "source /entrypoint.sh; rostopic pub --once /bebop/takeoff std_msgs/Empty"
sleep 10 # wait till drone is in the air
docker exec -it controller /bin/bash -c "source /entrypoint.sh; rostopic pub --once /bebop/land std_msgs/Empty"
```

this little script will let the drone take off and land 10 seconds later.

You should not be connected with any other interface than the WIFI. This can introduce bugs to the system and the drone cannot communicate annymore with the driver. Also after a disconnect of the drone, the Beebop driver must be restarted.
