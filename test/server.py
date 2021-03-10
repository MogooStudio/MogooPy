import socket


def init():
    s_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':
    init()