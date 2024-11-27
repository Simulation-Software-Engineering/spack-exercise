FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y apt-utils vim tmux htop git curl wget cmake build-essential sudo python3 python-is-python3 pkg-config python3-openssl bash gzip file openssl gnupg nano
RUN apt-get install -y libboost-filesystem-dev libboost-container-dev

# Cleanup
RUN apt-get clean
RUN rm -rf /tmp/*

# Create user
ARG USER_NAME=spackbuilder
ARG USER_HOME=/home/${USER_NAME}
#ARG USER_ID=1000
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g $GROUP_ID "$USER_NAME"
RUN adduser \
    --home "$USER_HOME" \
    --uid $USER_ID \
    --gid $GROUP_ID \
    --disabled-password \
    "$USER_NAME"

RUN echo "$USER_NAME" ALL=\(root\) NOPASSWD:ALL > "/etc/sudoers.d/$USER_NAME" && \
    chmod 0440 "/etc/sudoers.d/$USER_NAME"

USER "$USER_NAME"
WORKDIR "$USER_HOME"

ENV USER "$USER_NAME"
ENV LD_LIBRARY_PATH /usr/local/lib:"${LD_LIBRARY_PATH}"

# Set up Spack
COPY spack-config ${USER_HOME}/.spack
RUN git clone -b v0.23.0 -c feature.manyFiles=true --depth=2 https://github.com/spack/spack.git spack && echo ". ${USER_HOME}/spack/share/spack/setup-env.sh" >> ${USER_HOME}/.bashrc
RUN sudo chown -R $USER_NAME:$USER_NAME .spack && . ${USER_HOME}/spack/share/spack/setup-env.sh && spack spec yaml-cpp
RUN echo alias spack="/home/spackbuilder/spack/bin/spack" >> ~/.bashrc

# Bootstrap clingo
#COPY bootstrap-spack.sh ${USER_HOME}/bootstrap-spack.sh
#RUN su - $USER_NAME -c ./${USER_HOME}/bootstrap-spack.sh && rm bootstrap-spack.sh

CMD ["bash"]

# Reset frontend for interactive use
ENV DEBIAN_FRONTEND=
