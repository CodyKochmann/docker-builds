#!/bin/bash
# @Author: Cody Kochmann
# @Date:   2019-09-16 11:16:42
# @Last Modified by:   Cody Kochmann

#set -euxo

export FREE_DISK_MB='1024'
export LOG_PATH='/var/log/'

function show-disk-usage(){
    df -h "$LOG_PATH" | awk '{print($2 "\t" $3 "\t" $4)}' | xargs -n2 -d'\n' | awk '{print($1":"$4 "\t" $2":"$5 "\t" $3":"$6)}'
}

function current-disk-space(){
    df --output=avail --block-size=M "$LOG_PATH" | awk 'BEGIN {FS = "M"} ; /M/ {print($1)}'
}

function deletable-archives(){
    find "$LOG_PATH" -maxdepth 1 -type f -name '*.gz' -printf '%T+ %p\n'
}

function oldest-archive(){
    deletable-archives | sort | awk 'NR==1{print $2}'
}

function delete-oldest-archive(){
    oldest-archive | xargs -n 1 rm -vf
}

show-disk-usage

while [ "$(current-disk-space)" -lt "$FREE_DISK_MB" ] && [ "$(deletable-archives | grep . -c)" -gt 0 ]
do
    delete-oldest-archive && show-disk-usage
done
