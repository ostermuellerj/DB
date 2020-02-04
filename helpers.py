# Change string size
def fix_length(string, length):
    string = string.rstrip(" \n")
    if len(string) > length:
        print("Something is seriously wrong here.")
    else:
        diff = length - len(string)
        out_string = str(string) + " "*diff
        return out_string