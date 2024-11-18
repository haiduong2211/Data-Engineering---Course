# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  pattern = list(pattern)
  text = list(text)
  return result

def RabinKarp(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0 
    h = 1
    q = 101
    result = []
    if M > N:
        return [-1]
    for i in range(M-1):
        h = (h*d)%q
  
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
  
    for i in range(N-M+1):
        if p==t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                #print ("Pattern found at index " + str(i))
                result.append(i)
  
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
            # We might get negative values of t, converting it to positive
            if t < 0:
                t = t+q
    return result

d = 256


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = RabinKarp(pattern, text,d)
  print(" ".join(map(str, result)))
