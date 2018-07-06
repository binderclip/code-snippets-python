import time
from profilehooks import profile

class SampleClass:

    @profile
    def silly_fibonacci_example(self, n):
        """Return the n-th Fibonacci number.

        This is a method rather rather than a function just to illustrate that
        you can use the 'profile' decorator on methods as well as global
        functions.

        Needless to say, this is a contrived example.
        """
        if n < 1:
            raise ValueError('n must be >= 1, got %s' % n)
        if n in (1, 2):
            return 1
        else:
            return (self.silly_fibonacci_example(n - 1) +
                    self.silly_fibonacci_example(n - 2))


@profile
def f2():
    time.sleep(1)


if __name__ == '__main__':
    fib = SampleClass().silly_fibonacci_example
    print(fib(10))
    print(f2())

# ref: http://mg.pov.lt/profilehooks/
