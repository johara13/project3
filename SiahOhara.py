import Forest, Parser, Person
import sys
if __name__ == '__main__':

    f = Forest.Forest()
    p = Parser.Parser(f)

    for line in sys.stdin:
        newline = line.lower().split()
    
        print(newline)

        if newline[0] == 'e' and len(newline) >= 4:
            p.e(newline[1], newline[2], newline[3])
        elif newline[0]   == 'e' and len(newline) < 4:
            p.e(newline[1], newline[2])
        elif newline[0] == 'r':
            p.r(newline[1], newline[2])
        elif newline[0] == 'x':
            print('X')
        elif newline[0] == 'w':
            print(p.w(newline[1], newline[2]))

    f.debug()