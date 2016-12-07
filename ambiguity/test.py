def expand(grammar, symbol):
    result = []
    for rule in grammar:
        if rule[0] == symbol:
            result.append(rule[1])
    return result

def expand_first_nonterminal(grammar, string):
    result = []
    for i in xrange(len(string)):
        if isterminal(grammar, string[i]) == False:
            for j in expand(grammar, string[i]):
                result.append(string[:i]+j+string[i+1:])
            return result
    return None

def full_expand_string(grammar,string, result):
    for i in expand_first_nonterminal(grammar,string):
        if allterminals(grammar,i):
            result.append(i)
        else:
            full_expand_string(grammar,i,result)

def isterminal(grammar,symbol):
    for rule in grammar:
        if rule[0] == symbol:
            return False
    return True

def allterminals(grammar,string):
    for symbol in string:
        if isterminal(grammar,symbol) == False:
            return False
    return True

def returnall(grammar, start):
    result = []
    for rule in grammar:
        if rule[0] == start:
            if allterminals(grammar,rule[1]):
                return rule[1]
            else:
                full_expand_string(grammar, rule[1], result)
    return result

def isambig(grammar, start, utterance):
    count = 0
    for i in returnall(grammar,start):
        if i == utterance:
            count+=1
    if count > 1:
        return True
    else:
        return False


grammar1 = [
       ("S", [ "P", ]),
       ("S", [ "a", "Q", ]) ,
       ("P", [ "a", "T"]),
       ("P", [ "c" ]),
       ("Q", [ "b" ]),
       ("T", [ "b" ]),
       ]
print isambig(grammar1, "S", ["a", "b"])
print isambig(grammar1, "S", ["c"])
