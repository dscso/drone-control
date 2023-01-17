FROM ros:melodic

RUN apt-get update && apt-get install build-essential python3-rosdep python3-catkin-tools -y
RUN mkdir -p ~/bebop_ws/src
WORKDIR /root/bebop_ws
RUN git clone https://github.com/AutonomyLab/bebop_autonomy.git src/bebop_autonomy
RUN . /opt/ros/melodic/setup.sh &&\
    catkin_init_workspace
RUN rosdep update
RUN rosdep install --from-paths src -i -y
RUN . /opt/ros/melodic/setup.sh &&\
    catkin build

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]