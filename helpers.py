#Change line length for static line size
def lineset(line, length):
    line = line.rstrip()
    if len(line) > length:
        print("Something is seriously wrong here.")
    else:
        diff = length - len(line)
        new_line = str(line) + " "*diff + "\n"
        return new_line