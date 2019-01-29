import sys
opcode = {'NOP': '0',
          'LD': '1',
          'LDC': '2',
          'AND': '3',
          'ANDC': '4',
          'OR': '5',
          'ORC': '6',
          'XNOR': '7',
          'STO': '8',
          'STOC': '9',
          'IEN': 'A',
          'OEN': 'B',
          'JMP': 'C',
          'RTN': 'D',
          'SKZ': 'E'}
if len(sys.argv) > 1:
    path = sys.argv[1]
    sys.stdin = open(path, "r")
    pathout = path[:path.rfind('.')] + '_comp.txt'
    sys.stdout = open(pathout, 'w')
for line in sys.stdin:
    cline = line.split(';')[0].split()
    print(opcode[cline[0]],end='')
    if len(cline) > 1:
        print(cline[1],end='')
    else:
        print('0',end='')
