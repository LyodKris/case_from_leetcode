def HZ(n:int):
    res = n
    history = {n}
    while (True):
        n = str(res)
        res = 0
        for i in range(len(str(n))):
            res += int(n[i])**2
        if res == 1:
            return True
        if res in history:
            return False
        history.add(res)


        '''last = 0
        res = n
        history = {}
        history[n] = 0
        while (True):
            n = str(res)
            res = 0
            for i in range(len(str(n))):
                res += int(n[i])**2
            history[res] = 0
            if last == res or res == 1 or history[res] == 0:
                break
            last = res
        if res == 1:
            return True
        else:
            return False'''


if __name__ == "__main__":
    n = 2
    

    print(HZ(n))
