import numpy as np

def analisys_greedy(packets):
  m = len(packets)
  if(m == 0 or packets[0] != 1):
    print("ERROR")
    sys.exit(1)
  if(m <= 2): return True, None
  for cards in range(packets[2]+1, packets[m-1]+packets[m-2]):
    s1, q1 = greedy(cards, packets)
    s2, q2 = dynamic(cards, packets)
    if(np.not_equal(s1, s2).all()):
      return False, (cards, s1, s2)
  return True, None


def greedy(cards, packets):
  m = len(packets)
  Sol = np.zeros(m, np.int8)
  q = 0
  for c in range(m-1,-1,-1):
    size = packets[c]
    coef = cards // size
    cards -= coef * size
    Sol[c] = coef
    q += coef
  return Sol, q


def dynamic(cards, packets):
  m = len(packets)
  min_packets = np.zeros(cards + 1, np.int8)
  last_packet_idx = np.zeros(cards + 1, np.int8)
  for x in range(1, cards+1):
    current_min_packets = cards + 1
    current_last_packet_idx = -1
    for i in range(0, m):
      current_size = packets[i]
      if(x < current_size): break
      q = 1 + min_packets[x - current_size]
      if(q < current_min_packets):
        current_min_packets = q
        current_last_packet_idx = i
    min_packets[x] = current_min_packets
    last_packet_idx[x] = current_last_packet_idx
  S = np.zeros(m, np.int8)
  q = 0
  while(cards > 0):
    idx_packet = last_packet_idx[cards]
    size = packets[idx_packet]
    S[idx_packet] += 1
    cards -= size
    q += 1
  return S, q
