def aoc09():
    line = open("day9.input").read().strip()
    disk = sum( [[-1 if idx%2 else idx//2]*int(c) for (idx,c) in enumerate(line)],[])  # flattened
    fill = [x for x in disk[::-1] if x >= 0]
    print(sum(i*v if v>=0 else i*fill.pop(0) for (i, v) in enumerate(disk[:len(fill)])))

    # part 2
    L=[[],[]]
    pos = 0
    for idx,length in enumerate(map(int, line)):
        L[idx%2].append((pos,length))                 #L[0]: data, L[1]: free space
        pos += length
    for i,(dpos,dlen) in list(enumerate(L[0]))[::-1]: # look at data starting right
        for j,(spos, slen) in enumerate(L[1]):        # look at free space starting left
            if spos < dpos and slen >= dlen:          # can move data to free space
                L[0][i] = (spos, dlen)
                L[1][j] = (spos + dlen, slen - dlen)  # may create 0-length free space block, but that's ok
                break
    print(sum(v*dlen*(2*dpos + dlen - 1) for v, (dpos, dlen) in enumerate(L[0]))//2)  # look at my fancy ma

aoc09()