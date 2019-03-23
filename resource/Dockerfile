FROM debian as builder

# Builder Setup
RUN apt update
RUN apt install -y build-essential

# Compiling Steps
RUN mkdir /build
RUN mkdir /birthday-present
WORKDIR /build
COPY main.c .
RUN gcc -O3 -o /birthday-present/main -static main.c

# Permissions (need to be set here since scratch containers dont have shells)
# only user read and execute of executable
RUN chmod 500 /birthday-present/main
# disable permissions for the build directory since no one needs to access it
RUN chmod 000 /birthday-present

# Install to Scratch
FROM scratch
# import the generated bin directory
COPY --from=builder /birthday-present /bin
# make the workdir the immutable bin directory
WORKDIR /bin
# for some reason path is preset in docker, so clear it without using a shell
# (if you have a better way, lemme know)
ENV PATH=

# set the entrypoint
CMD ["/bin/main"]
