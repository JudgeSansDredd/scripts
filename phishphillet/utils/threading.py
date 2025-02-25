import threading


def startThreads(num_threads, target_fn):
    threads = []
    for i in range(num_threads):
        t = threading.Thread(
            target=target_fn,
            name=f"Thread_{i}"
        )
        t.daemon = True
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

