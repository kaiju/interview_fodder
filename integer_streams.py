#!/usr/bin/env python3

"""
The Problem:

Combine three "streams" of integers and implement a getNextInt() function that returns the
next lowest integer across all streams.

Example Code:

public interface IntStream {
  #always returns an int strictly greater than the previous int it returned.
  public int getNextInt()
}

Class IntStreamMerger implements IntStream {
  List<IntStream> streams;
   
  public IntStreamMerger(List<IntStreams> streams) {
    this.streams = streams
  }
 
  public int getNextInt() {
    #implement this method.   
  }
}

Example Input:

Stream 1: 3, 15, 40, 100
Stream 2: 20, 21, 46, 59
Stream 3: 2, 102, 190, 1000

Expected Output:

2, 3, 15, 20, 21, 40, 46, 59, 100, 102, 190, 1000

"""

class IntStream(object):
    """ A single 'stream' of integers """
    ints = None

    def __init__(self, iterable):
        self.ints = list(iterable)

    def getNextInt(self):
        return self.ints.pop(0)

class IntStreamMerger(object):
    """ Represents a collection of IntStreams """

    streams = None
    stream_ids = None
    stream_items = None

    def __init__(self, streams):
        # All our Integer Streams
        self.streams = streams

        # A list of tuples representing the next integers for each stream (stream id, int value)
        self.next_stream_integers = []

        # A list of stream ids we have the next integers for
        # This is so we can easily check if we have an integer value for a stream without having
        # to iterate each tuple in `next_stream_integers`
        self.streams_with_next_integers = []

    def getNextInt(self):
        """ Get the next Integer from our collection of integer streams """

        # Iterate over every stream we don't have a next integer for
        for stream in [s for s in self.streams if id(s) not in self.streams_with_next_integers]:

            # Attempt to get the next integer from the stream
            try:
                next_int = stream.getNextInt()
            except IndexError as e:
                # IndexError means we've exhausted the stream/it doesn't have an int for us right now
                # Were these for real actual streams getting data continually added to them, we'd just
                # revisit them on the next IntStreamMerger.getNextInt() call.
                continue

            # add stream id to stream ids we have next ints for
            self.streams_with_next_integers.append(id(stream))              

            # add tuple into stream items
            self.next_stream_integers.append((id(stream), next_int))

        # sort our list of next integers from each stream so the smallest int is always first
        self.next_stream_integers.sort(key=lambda s: s[1])

        # pop the smallest (first) integer value off our stream_items list
        try:
            next_int_stream = self.next_stream_integers.pop(0)
        except IndexError as e:
            # we totally exhausted all int streams, return None
            return None

        # Remove the stream we're returning an int from
        self.streams_with_next_integers.remove(next_int_stream[0])

        return next_int_stream[1]

if __name__ == "__main__":

    streams = IntStreamMerger([
        IntStream([3, 15, 40, 100]),
        IntStream([20, 21, 46, 59]),
        IntStream([2, 102, 190, 1000])
    ])

    while True:
        next_int = streams.getNextInt()

        if next_int is not None:
            print(next_int)
        else:
            break
