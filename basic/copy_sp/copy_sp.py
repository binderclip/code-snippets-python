import copy


def shallow_copy():
    print('=== shallow_copy ===')
    d1 = {'a': 1}
    print(f'd1: {d1}')
    d2 = d1.copy()
    print(f'd2: {d2}')
    d2['a'] = 2
    d2['b'] = 3
    print(f'd2: {d2}')
    print(f'd1: {d1}')

    d3 = {'d': d1}
    print(f'd3: {d3}')
    d4 = d3.copy()
    print(f'd4: {d4}')
    d1['a'] = 2
    print(f'd3: {d3}')
    print(f'd4: {d4}')


def deep_copy():
    print('=== deep_copy ===')
    d1 = {'a': 1}
    d2 = {'b': d1}
    d3 = {'c': d2}
    d4 = copy.deepcopy(d3)
    print(f'd3: {d3}')
    print(f'd4: {d4}')
    d3['c']['b']['a'] = 2
    print(f'd2: {d2}')
    print(f'd3: {d3}')
    print(f'd4: {d4}')


def main():
    shallow_copy()
    deep_copy()


if __name__ == '__main__':
    main()
