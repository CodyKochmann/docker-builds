import os
from queue import Queue, Empty
from contextlib import contextmanager

__script_dir__ = os.path.dirname(os.path.abspath(__file__))

bash = lambda c: os.popen(c).read().strip()
bash = lambda i: print('bash: {}'.format(i))
class IterableQueue(Queue):
    def __iter__(self):
        while True:
            try:
                yield self.get_nowait()
            except Empty:
                break
@contextmanager
def pushd(d):
    previous = os.getcwd()
    os.chdir(d)
    try:
        yield
    finally:
        os.chdir(previous)

def is_docker_dir(i:str)->bool:
    return os.path.isdir(i) and 'Dockerfile' in os.listdir(i)
    
def docker_from(docker_dir:str)->str:
    assert is_docker_dir(docker_dir)
    with open(os.path.join(docker_dir, 'Dockerfile'), 'r') as f:
        for line in f:
            if line.startswith('FROM '):
                return line[5:].strip()
    assert 0, 'couldnt find a FROM line for {}'.format(docker_dir)
        
with pushd(__script_dir__):

    docker_dirs = {i for i in os.listdir('.') if is_docker_dir(i)}
    
    
    update_q = IterableQueue()
    for i in docker_dirs:
        update_q.put(i)
        
    #print(docker_dirs)
    
    for i in update_q:
        parent_docker = docker_from(i)
        if parent_docker.startswith('codykochmann/'):
            parent_docker = parent_docker.split('codykochmann/')[1]
        if parent_docker in docker_dirs:
            update_q.put(i) # re-queue since its parent hasnt been updated yet
        else:
            docker_dirs.remove(i)
            with pushd(i):
                print('building {}...'.format(i))
                bash('docker build -t {} .'.format(i))
                print('pushing {}...'.format(i))
                bash('docker push {}'.format(i))

