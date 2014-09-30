

def motif(s,t):
    matches = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            matches.append(i+1)
    return matches
