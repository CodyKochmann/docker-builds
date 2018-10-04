#!/bin/bash
function build-and-push(){
  pushd $1 ;
  docker build -t codykochmann/$1 . ;
  docker push codykochmann/$1 ;
  popd ;
}

function run(){
  find . -type d | fgrep -v git | fgrep '/' | sed 's|\./||g' | xargs build-and-push
}

run
run
