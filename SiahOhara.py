#!/usr/bin/python3

import Forest, Parser, Person
import sys

if __name__ == '__main__':

    f = Forest.Forest()
    p = Parser.Parser(f)

    for line in sys.stdin:
        
        newline = line.lower().split()

        if len(newline) < 2:
            continue
        else:
            if line[-1] == '\n':
                print(line[:-1])
            else: 
                print(line)

        if newline[0] == 'e' and len(newline) >= 4:
            p.e(newline[1], newline[2], newline[3])
        elif newline[0]   == 'e' and len(newline) < 4:
            p.e(newline[1], newline[2])
        elif newline[0] == 'r':
            answer = p.r(newline[1], newline[2])
            if answer is not None:
                print(str(answer))
        elif newline[0] == 'x':
            if newline[2] != 'cousin':
                answer = p.x(newline[1], newline[2], newline[3])
            else:
                rel = [newline[2], int(newline[3]), int(newline[4])]
                answer = p.x(newline[1], rel, newline[5])
            if answer is not None:
                print(str(answer))
        elif newline[0] == 'w':
            if newline[1] != 'cousin':
                answer = p.w(newline[1], newline[2])
                if answer is not None:
                    print(str(answer))
            else:  # if the relation is cousin passes 'cousin # #' as a list for the first argument
                answer = p.w([newline[1], int(newline[2]), int(newline[3])], newline[4])
                print(str(answer))
        
        print()
    # print(f.isRelatedTo('a', 'b'))