def extract_escape(x:str):
    if len(x) == 0:
        return x
    while x[0] == " ":
        xl=list(x)
        xl.pop(0)
        x="".join(xl)
        if x == "":
            return x
    while x[-1] == " ":
        xl=list(x)
        xl.pop(-1)
        x="".join(xl)
        if x == "":
            return x
    return x