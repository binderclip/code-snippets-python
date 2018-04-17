import datetime


def main():
    dt = datetime.datetime.utcnow()
    print(dt)
    print(dt.isoformat())

if __name__ == '__main__':
    main()
