#1
def check_coupon(code, valid, cur, exp):
    m = ["Ja","Fe","Ma","Ap","Ma","Ju","Ju","Au","Se","Oc","No","De"]
    cur, exp = cur.split(), exp.split()
    
    if code != valid or type(code) != type(valid) or int(cur[2]) > int(exp[2]) or \
    cur[2] == exp[2] and m.index(cur[0][:2]) > m.index(exp[0][:2]) or \
    cur[2] == exp[2] and m.index(cur[0][:2]) == m.index(exp[0][:2]) and \
    int(cur[1][:-1]) > int(exp[1][:-1]):
        return False
    return True
