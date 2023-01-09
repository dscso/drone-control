FROM ros:foxy-ros1-bridge-focal

RUN apt-get update && apt-get install -y supervisor

COPY ./*.sh /
RUN chmod +x /*.sh

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
