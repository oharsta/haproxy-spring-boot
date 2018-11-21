from haproxyadmin import haproxy


def info():
    hap = haproxy.HAProxy(socket_dir="/usr/local/var/run", socket_file="haproxy.sock")
    backends = hap.backends()
    print([b.name for b in backends])
    # nodes = next(b for b in backends if b.name == "nodes")
    nodes = hap.backends("nodes")[0]
    print([s.name for s in nodes.servers()])
    # web01 = next(s for s in nodes.servers() if s.name == 'web01')
    web01 = nodes.servers("web01")[0]
    print(web01.weight)
    web02 = next(s for s in nodes.servers() if s.name == 'web02')
    print(web02.weight)
    # web01.setweight(100)


if __name__ == "__main__":
    info()
