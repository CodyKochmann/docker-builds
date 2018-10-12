import os
from queue import Queue, Empty
from contextlib import contextmanager

__script_dir__ = os.path.dirname(os.path.abspath(__file__))

def bash(command:str) -> str:
    ''' this executes a command and streams the output to the same line '''
    print('running:', repr(command))
    out = []
    previous_len = 0
    for line in os.popen(command):
        line = line.strip()
        out.append(line)
        print(line+(' '*(previous_len-len(line))), end='\r')
        previous_len = len(line)
    print('') # preserve the last line in the terminal
    return '\n'.join(out).strip()

class IterableQueue(Queue):
    def __iter__(self):
        while True:
            try:
                yield self.get_nowait()
            except Empty:
                break

@contextmanager
def pushd(d:str):
    previous = os.getcwd()
    os.chdir(d)
    try:
        yield
    finally:
        os.chdir(previous)

def is_docker_dir(i:str) -> bool:
    return os.path.isdir(i) and 'Dockerfile' in os.listdir(i)

def docker_from(docker_dir:str) -> str:
    assert is_docker_dir(docker_dir)
    with open(os.path.join(docker_dir, 'Dockerfile'), 'r') as f:
        for line in f:
            if line.startswith('FROM '):
                return line[5:].strip()
    assert 0, 'couldnt find a FROM line for {}'.format(docker_dir)

with pushd(__script_dir__):

    docker_dirs = (i for i in os.listdir('.') if is_docker_dir(i))
    updated_containers = set()
    update_q = IterableQueue()

    for i in docker_dirs:
        update_q.put(i)

    for i in update_q:
        parent = docker_from(i)
        if parent.startswith('codykochmann/') and parent.split('codykochmann/')[1] not in updated_containers:
            update_q.put(i) # re-queue since its parent container hasnt been updated yet
        else:
            updated_containers.add(i)
            with pushd(i):
                print('building {}...'.format(i))
                bash('docker build --no-cache -t codykochmann/{}:latest .'.format(i))
                print('pushing {}...'.format(i))
                bash('docker push codykochmann/{}:latest'.format(i))
