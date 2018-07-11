import requests


def main():
    r = requests.get('https://httpbin.org/get')
    print(r.content)    # """Content of the response, in bytes."""
    print(r.text)       # """Content of the response, in unicode...."""
    print(r.json())     # """Returns the json-encoded content of a response, if any....
                        # raises ValueError: If the response body does not contain valid json."""

    r = requests.get('https://httpbin.org/')
    try:
        print(r.json())
    except ValueError as e:
        print(type(e))
        print(e)

if __name__ == '__main__':
    main()
