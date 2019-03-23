# resource containers

A tiny scratch based container that blocks forever.

#### quick start
```bash
# pull the latest image
docker pull codykochmann/resource

# generalize the name so stats are cleaner
docker tag codykochmann/resource resource

# explore the unexpected benefits of dedicated resource containers
docker run -d --restart always --cap-drop all --read-only --name host-net --network host resource
```

At first this was just an experiment I was doing to see alternative ways to share resources between containers, but then I lived with it for a while.

This winds up unlocking a lot of functionality that wasn't really supported by docker. 

### Example 1: Sharing the host network with multiple unprivileged containers.

Terminal 1:

```bash
docker run --network host --name host-net --detatch --restart always --cap-drop all --read-only codykochmann/resource
```

Terminal 2:

```bash
docker run -it --rm --network container:host-net alpine
/ # ifconfig
```

Terminal 3 (while Terminal 2 is still open):

```bash
docker run -it --rm --network container:host-net codykochmann/packetbeat
```

> Normally docker will refuse to allow you to connect multiple containers to the host, this enables unlimited.

### Example 2: Use anonymous volumes that can survive pruning even if your application container is off.

```bash
docker run -v /var/log --name internal-logs -d --restart always --cap-drop all --read-only codykochmann/resource
```

```bash
docker run --name gitlab --volumes-from internal-logs -d --restart always gitlab/gitlab-ce:latest
```

```bash
# now I can find out how many logs ive missed out on since not all logs go to stdout 
docker run --volumes-from internal-logs codykochmann/multitail /var/log/gitlab
```

So now, if we decide we dont need certain containers running ALL the time because we would like to use the freed up RAM, you can simply `docker stop gitlab` and leave it stopped until we are ready to use it again.

At first this felt like an edge case but I like being able to run `docker volume prune` and `docker system prune` to quickly get a chunk of my disk back. With little `resource` containers now preserving important (but currently unused) networks and volumes, I can now fully take advantage of the prune system docker is great for without needing to worry about losing important pieces of data. 

#### Note

I've seen this done with both the `busybox` and the `alpine` image as the placeholder but since the concept of a resource is that it is as light and dumb as possible so you dont notice how many you really have, thus your decisions focus more towards how many segmentations of your resources you actually need, instead of can afford.

Here's a brief look at where the `resource` container lands in comparrison to the other commonly used placeholder images. 

| image                 | image size | lowest observed RAM footprint (without system tweaks) |
|:----------------------|:-----------|:--------------------------------------------------------|
| alpine                | 5.53MB     | 376KiB                                                |
| busybox               | 1.2MB      | 276KiB                                                |
| codykochmann/resource | 810kB      | 216KiB                                                |

