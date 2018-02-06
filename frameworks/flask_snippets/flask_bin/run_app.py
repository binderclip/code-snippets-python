# coding: utf-8
from app import app


def main():
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
