FROM rust:latest as builder

RUN git clone https://github.com/toshi-search/Toshi.git
RUN rustup component add rustfmt --toolchain 1.42.0-x86_64-unknown-linux-gnu
RUN cd Toshi && cargo build


FROM debian:buster-slim

COPY ./config.toml /config/config.toml
COPY --from=builder /Toshi/target/debug/toshi /bin/toshi

CMD ["/bin/toshi"]
