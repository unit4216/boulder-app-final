
last_100_requests = []


def add_processing_time(processing_time: float):
    last_100_requests.append(processing_time)
    if len(last_100_requests) > 100:
        last_100_requests.pop(0)


def get_average_processing_time():

    if len(last_100_requests) == 0:
        return 0

    total_processing_time = 0
    for req in last_100_requests:
        total_processing_time += req
    total_time_in_ms = total_processing_time * 1000
    return total_time_in_ms / len(last_100_requests)
