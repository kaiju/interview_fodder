#!/usr/bin/env

"""
The Problem:

We want to store a file in memcached, regardless of size. Implement a function to store the file into memcache
and a function to retrieve it back from memcache.

Example Input:

dd if=/dev/random of=big_file.dat bs=1024 count=100

"""
from pymemcache.client.base import Client
import os.path, sys

client = Client(('localhost', 11211))

def set_file(filename):
    """ chunk up a file and shove it into memcache """

    file_to_chunk = open(filename, 'r')
    chunk_index = 0

    while True:
        chunk = file_to_chunk.read(1024)

        if chunk == '': # hit EOF
            break

        prefix = '{}:chunk:{}'.format(os.path.basename(filename), chunk_index)

        client.set(prefix, chunk)

        chunk_index += 1

    client.set('{}:chunks'.format(os.path.basename(filename)), chunk_index)

def get_file(filename):
    """ take a filename and pull the chunks out of memcache and write to a new file """

    total_chunks = int(client.get('{}:chunks'.format(os.path.basename(filename))))

    my_new_file = open('{}.retrieved'.format(os.path.basename(filename)), 'w')

    for chunk_index in range(total_chunks):
        chunk = client.get('{}:chunk:{}'.format(os.path.basename(filename), chunk_index))
        my_new_file.write(chunk)

    my_new_file.flush()
    my_new_file.close()

if __name__ == "__main__":
    set_file(sys.argv[1]) # shove it into memcache

    get_file(sys.argv[1]) # pull it out of memcache and write it to a file
