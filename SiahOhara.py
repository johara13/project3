import Forest, Parser, Person
import sys
if __name__ == '__main__':

  f = Forest.Forest()
  p = Parser.Parser(f)

  for line in sys.stdin:
    newline = line.split()
    
    if newline[0]   == 'E' and len(newline) >= 4:
        p.e(newline[1], newline[2], newline[3])
    elif newline[0]   == 'E' and len(newline) < 4:
        p.e(newline[1], newline[2])
    elif newline[0] == 'R':
        print('R')
    elif newline[0] == 'X':
        print('X')
    elif newline[0] == 'W':
        print('W')