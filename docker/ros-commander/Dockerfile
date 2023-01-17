FROM ros:melodic

#RUN apt-get update && apt-get install build-essential python3-rosdep python3-catkin-tools -y

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]