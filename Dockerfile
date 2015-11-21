FROM andrewosh/binder-base

USER root
RUN apt-get install auto-07p

USER main
ENV PYTHONPATH=/usr/lib/auto-07p/python$PYTHONPATH