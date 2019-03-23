FROM debian as builder
RUN apt update
RUN apt install -y build-essential
WORKDIR /
COPY main.c .
RUN gcc -O3 -o main -static main.c

FROM scratch
WORKDIR /
COPY --from=builder /main .
ENTRYPOINT ["./main"]
