import time

import random
from retrying import retry


def unreliable_work():
    print(f'work at {time.time()}')
    if random.randint(0, 10) > 1:
        print('failed')
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"


def unreliable_work2():
    print(f'work at {time.time()}')
    if random.randint(0, 10) > 7:
        raise ValueError("Too high")
    elif random.randint(0, 10) > 1:
        print('failed')
        raise IOError("Broken sauce, everything is hosed!!!111one")
    else:
        return "Awesome sauce!"



@retry
def never_give_up_never_surrender():
    # Retry forever ignoring Exceptions, don't wait between retries
    print('=== never_give_up_never_surrender ===')
    return unreliable_work()


@retry(stop_max_attempt_number=6)
def stop_after_6_attempts():
    # Stopping after 6 attempts
    print("=== stop_after_6_attempts ===")
    return unreliable_work()

i = 0

@retry(stop_max_delay=3000)
def stop_after_3_s():
    # Stop after the time from the first attempt >= stop_max_delay.
    print("=== stop_after_3_s ===")
    time.sleep(1.1)
    global i
    i += 1
    raise IOError(f"read timeout No.{i}")


@retry(wait_fixed=2000)
def wait_2_s():
    # Wait 2 second between retries
    print('=== wait_2_s ===')
    print(unreliable_work())


@retry(wait_random_min=1000, wait_random_max=2000)
def wait_random_1_to_2_s():
    # Randomly wait 1 to 2 seconds between retries
    print('=== wait_random_1_to_2_s ===')
    print(unreliable_work())


@retry(wait_exponential_multiplier=100, wait_exponential_max=1000)
def wait_exponential_100():
    # Wait 2^x * 100 milliseconds between each retry, up to 1 seconds, then 1 seconds afterwards
    print('=== wait_exponential_100 ===')
    print(unreliable_work())


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)


@retry(retry_on_exception=retry_if_io_error)
def might_io_error():
    # Retry forever with no wait if an IOError occurs, raise any other errors
    print('=== might_io_error ===')
    print(unreliable_work2())


@retry(retry_on_exception=retry_if_io_error, wrap_exception=True)
def only_raise_retry_error_when_not_io_error():
    # Retry forever with no wait if an IOError occurs, raise any other errors wrapped in RetryError
    print('=== only_raise_retry_error_when_not_io_error ===')
    print(unreliable_work2())


def main():
    print(never_give_up_never_surrender())
    # print(stop_after_6_attempts())      # sometimes OK, sometimes not OK
    # stop_after_3_s()
    # wait_2_s()
    # wait_random_1_to_2_s()
    # wait_exponential_100()
    # might_io_error()
    # only_raise_retry_error_when_not_io_error()


if __name__ == '__main__':
    main()
