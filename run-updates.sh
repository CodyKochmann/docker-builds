#!/bin/bash
function build-and-push(){
  docker image rm codykochmann/$i ;
  pushd $1 ;
  docker build -t codykochmann/$1 . ;
  docker push codykochmann/$1 ;
  popd ;
}

function run(){
  for i in $(find . -type d | fgrep -v git | fgrep '/' | sed 's|\./||g')
  do
    build-and-push $i
  done
}

run
run
