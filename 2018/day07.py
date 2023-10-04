data = [line.rstrip("\n") for line in open("input07.txt")]

req = {}
for line in data:
    line = line.split(" ")
    if line[1] not in req:
        req[line[1]] = set()
    if line[7] not in req:
        req[line[7]] = set()

    req[line[7]].add(line[1])

def get_available(req, done, started):
    a = []
    for k,v, in req.items():
        if k not in done and k not in started and not v:
            a.append(k)

    return sorted(a)

done = set()
started = []
workers = [("", 0) for _ in range(5)]
step = 0
while len(done) < len(req) + 1:
    open_workers = []
    for i, w in enumerate(workers):
        if w[1] <= 0:
            open_workers.append(i)

            done.add(w[0])

            for s in req.values():
                s.discard(w[0])

    for i in open_workers:
        a = get_available(req, done, started)

        if len(a) > 0:
            workers[i] = (a[0], ord(a[0]) - ord("A") + 61)
            started.append(a[0])

    for i, w in enumerate(workers):
        workers[i] = (w[0], w[1] - 1)

    step += 1

    print(workers)


print(step - 1)



# part 1
def get_order(req):
    done = []
    while len(done) < len(req):
        a = get_available(req, done, [])

        for s in req.values():
            s.discard(a[0])

        done.append(a[0])

    return "".join(done)

    
