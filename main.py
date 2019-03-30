from State import *

grid = \
"""
BBBBBBB
BBFFFBB
BUFFFXB
BBFFFBB
BBBBBBB
""".strip()

grid2 = \
"""
BBBBBBBBB
BBFFFBFBB
BUFBFBFXB
BBFBFFFBB
BBBBBBBBB
""".strip()

grid3 = \
"""
BBBBBBBBB
BBFSSBFBB
BUFBSBFXB
BBFBFSFBB
BBBBBBBBB
""".strip()

grid4 = \
"""
BBBBBBBBBBBB
BBFFSSFFFFBB
BUFFFFFFFFXB
BBFFFFFFFFBB
BBFFFFFFFFBB
BBBBBBBBBBBB
""".strip()

grid5 = \
"""
BBBBBBBBBBB
BBFFFSSFFBB
BUFFFFFFFXB
BBFFSFFSSBB
BBFFFFFSFBB
BBBBBBBBBBB
""".strip()

grid6 = \
"""
BBBBBBBBB
BWHSSFFHB
BSFFFFFSB
BSHFFHFSB
BUFSBFFXB
BFFSWFSFB
BHFFHFSHB
BSSFKFFFB
BBBBBBBBB
""".strip()

puzzle1 = \
"""
BBBBBBBB
BsFsssBB
BsssssBB
BUffffXB
BsFFsfBB
BssfssBB
BBBBBBBB
""".strip()

puzzle2 = \
"""
BBBBBBBB
BRVFRHBB
BFRFVFBB
BUVFFFXB
BFHFVFBB
BFFFRHBB
BBBBBBBB
""".strip()

puzzle3 = \
"""
BBBBBBBB
BFFFFFBB
BF8s8FBB
BUsFsFXB
BF2s2FBB
BFFFFFBB
BBBBBBBB
""".strip()


max_health = 2
curr_health = max_health

if __name__ == '__main__':
  s = State(curr_health, max_health, exp=0, needed_exp=20, streak=0, grid_string=puzzle3)
  q = []
  hq.heappush(q, s)
  curr = s
  count = 0
  maxXP = 0
  while q:
    maxXP = max(maxXP, curr.exp)
    count += 1
    curr = hq.heappop(q)
    #print(curr)
    print(maxXP)
    print(count)
    if curr.win():
      print("WINNER:", curr.path)
      print(curr)
      q = []
      exit()
    for newState in curr.next_states():
      hq.heappush(q, (newState))
    # q.extend(curr.next_states())
  print("No path to exit with min. xp", s.needed_exp, "exists! :(")