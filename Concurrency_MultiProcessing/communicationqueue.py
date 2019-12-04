"""
Run from terminal.
Inter Process communication (IPC).
"""
# Queue class is a near clone to Queue found in queue module
from multiprocessing import Process, Queue
from time import sleep

SENTINEL = -1  # Sentinel value to kill the consumer process


def producer(data_, queue_):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing.
    """
    for item in data_:
        # put() add data to the queue
        queue_.put(item)

        print('Put data {} on the queue.'.format(item))

    queue_.put(SENTINEL)  # Adding sentinel item for the example
    print('Added sentinel value {} to the queue.'.format(SENTINEL))


def consumer(queue_):
    """
    Consumes some data and works on it.
    """
    while True:
        # Get data from the queue
        data_ = queue_.get()

        print('Data found to be processed: {}'.format(data_))

        if data_ is SENTINEL:
            break


if __name__ == '__main__':
    # Queue object
    queue = Queue()

    data = [n * 5 for n in range(10)]

    proc_producer = Process(target=producer, args=(data, queue))
    proc_consumer = Process(target=consumer, args=(queue,))
    proc_producer.start()
    proc_consumer.start()

    # Returns True if queue is empty
    print('Queue is empty: {}'.format(queue.empty()))
    sleep(0.001)
    print('Queue is empty: {}'.format(queue.empty()))

    # Indicate that no more data will be put on this queue by the current
    # process
    queue.close()

    # Join the background thread, it blocks until the background thread exits
    queue.join_thread()

    proc_producer.join()
    proc_consumer.join()
