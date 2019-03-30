from Tiles import *
from copy import deepcopy

"""
State - current kill streak, enemy positions, path taken to reach, health, exp
      - direction enemies facing, leashed places
Each state is a node
Only states that you can reach from each other are connected in the graph
Run djikstra's to reach a state where you've won from the beginning state
"""

dir_map = {
  (0, 1): 'D ',
  (0, -1): 'U ',
  (-1, 0): 'L ',
  (1, 0): 'R ',
}

class State:
  def __init__(self, curr_hp, max_hp, exp, needed_exp, streak, coins=0, poison=0, barked=0, path="", grid_string=None):
    self.curr_hp = curr_hp
    self.max_hp = max_hp
    self.exp = exp
    self.needed_exp = needed_exp
    self.streak = streak
    self.coins = coins
    self.poison = poison
    self.barked = barked
    self.tiles = []
    self.path = path

    self.is_win = False
    if grid_string:
      assert grid_string.count('U') == 1
      self.tiles = []
      self.player_pos = (-1, -1)
      for y, row in enumerate(grid_string.splitlines()):
        self.tiles.append(list(map(to_tile, row)))
        if 'U' in row:
          x = row.index('U')
          self.player_pos = (x, y)
      print(self.player_pos)
      print(self)

  """
  Order states by highest xp first
  """
  def __lt__(st1, st2):
    return st2.exp < st1.exp

  def get_tile(self, x, y):
    try:
      return self.tiles[y][x]
    except IndexError:
      return None

  def set_tile(self, x, y, tile):
    try:
      self.tiles[y][x] = tile
    except IndexError:
      pass

  def next_states(self):
    """
    Should return an iterator of possible future states
    """
    for direction in [(0, 1), (0, -1), (-1, 0), (1,0)]:
      new_pos = self.player_pos[0] + direction[0], self.player_pos[1] + direction[1]
      tile = self.get_tile(*new_pos)

      dir = dir_map.get(direction)

      new_state = State(self.curr_hp, self.max_hp, self.exp, self.needed_exp, self.streak, self.coins, self.poison, path=self.path + dir)
      new_state.tiles = deepcopy(self.tiles)
      new_state.player_pos = new_pos
      new_state.set_tile(*new_pos, Player())
      new_state.set_tile(*self.player_pos, Leash())
      new_state.is_win = False

      # can't step on these tiles
      if type(tile) in {Barrier, Leash}:
        new_state = None

      elif type(tile) is Floor:
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3

      elif type(tile) is Health:
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.curr_hp = new_state.max_hp - new_state.poison

      elif type(tile) is Snake:
        if self.curr_hp == self.max_hp - self.poison: # health filled up
          currentHP = self.curr_hp - 1
        else:
          currentHP = self.curr_hp
        new_state.curr_hp = currentHP
        new_state.exp += 1
        new_state.poison += 1
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.streak += 1

      elif type(tile) is Spider:
        new_state.curr_hp -= 1
        new_state.exp += 1
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.streak += 1

      elif type(tile) is SmallSpider:
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.streak += 1

      elif type(tile) is RedSpider:
        if new_state.streak == 3: #flipped over
          new_state.streak = 0
          new_state.exp += 3 + 2
        else: # not flipped over
          new_state.exp += 1
          new_state.curr_hp -= 2
        new_state.streak += 1

      elif type(tile) is Vampire:
        if new_state.curr_hp == 0: # vampire asleep
          new_state.exp += 5
        else: #vampire awake
          new_state.exp += 1
          new_state.curr_hp = 0
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.streak += 1

      elif type(tile) is KingSpider:
        new_state.curr_hp -= 1
        new_state.exp += 3
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        new_state.streak += 1

      elif type(tile) is Exit:
        if new_state.streak == 3:
          new_state.streak = 0
          new_state.exp += 3
        if self.exp < self.needed_exp:
          continue
        new_state.is_win = True

      if new_state and new_state.curr_hp >= 0 and new_state.hasPathToExit():
        yield new_state

  def hasPathToExit(self):
    return True

  def win(self):
    return self.is_win

  def __str__(self):
    head = """
    Exp: {}
    Health: {}
    """.strip().format(self.exp, self.curr_hp)
    rows = [head]
    for row in self.tiles:
      rows.append(' '.join(map(str, row)))
    return '\n'.join(rows)
