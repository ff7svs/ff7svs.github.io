
printBR = 2

f = open("tmp.txt", "r")
s = open("tmp.md", "w")

lines = f.readlines()

lastIsNewLine = 0
printNewLine= False

for line in lines:
    line = line.strip()
    if len(line) == 0:
        lastIsNewLine += 1
        if lastIsNewLine == printBR:
            s.write('<br>\n\n')
    else:
        lastIsNewLine = 0
        line = line.strip()
        line.replace("~", "～")
        if line == '***\n':
            continue
        elif len(line) < 8 and (
             (line[0], line[-1]) == ('[',']') or \
             (line[0], line[-1]) == ('【','】') or \
             (line[0], line[-1]) == ('（','）') or \
             (line[0], line[-1]) == ('-','-') or \
             (line[0], line[-1]) == ('第','章') or \
             (len(line) < 3) or \
             tuple(line[0:3].upper()) == ('V','O','L') or \
             (line[0].isdigit() and len(line) <= 3)) or \
             (len(line) > 6 and line[0:7] == 'Episode'):
            s.write('#### ' + line)
        else:
            s.write(line)
        s.write('\n\n')
    line = f.readline()
f.close()
s.close()
