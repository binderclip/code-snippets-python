# coding: utf-8
import statsd


def main():
    c = statsd.StatsClient('localhost', 8125)
    c.incr('foo')  # Increment the 'foo' counter.
    c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.


if __name__ == '__main__':
    main()
