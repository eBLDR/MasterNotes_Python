"""
Run from terminal.
Inter Process communication (IPC).
"""
from time import sleep

# Queue class is a near clone to Queue found in queue module
from multiprocessing import Process, Queue

sentinel = -1  # Sentinel value to kill the consumer process


def producer(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing.
    """
    for item in data:
        # put() add data to the queue
        q.put(item)

        print('Put data {} on the queue.'.format(item))

    q.put(sentinel)  # Adding sentinel item for the example
    print('Added sentinel value {} to the queue.'.format(sentinel))


def consumer(q):
    """
    Consumes some data and works on it.
    """
    while True:
        # Get data from the queue
        data = q.get()

        print('Data found to be processed: {}'.format(data))

        if data is sentinel:
            break


if __name__ == '__main__':
    # Queue object
    q = Queue()

    data = [n * 5 for n in range(10)]

    proc_producer = Process(target=producer, args=(data, q))
    proc_consumer = Process(target=consumer, args=(q,))
    proc_producer.start()
    proc_consumer.start()

    # Returns True if queue is empty
    print('Queue is empty: {}'.format(q.empty()))
    sleep(0.001)
    print('Queue is empty: {}'.format(q.empty()))

    # Indicate that no more data will be put on this queue by the current
    # process
    q.close()

    # Join the background thread, it blocks until the background thread exits
    q.join_thread()

    proc_producer.join()
    proc_consumer.join()
