from pprint import pprint
from itertools import product
from copy import deepcopy
import heapq as hq


class Tile:
  def __init__(self, direction=None):
    pass

def to_tile(character):
  return tile_map.get(character, Barrier)()

class Player(Tile):
  def __str__(self):
    return "U"

class TurtleUp(Tile, 0):
  def __str__(self):
    return "8"

class TurtleRight(Tile, 1):
  def __str__(self):
    return "6"

class TurtleDown(Tile, 2):
  def __str__(self):
    return "2"

class TurtleLeft(Tile, 3):
  def __str__(self):
    return "4"

class ZombieTurtleUp(Tile, 0):
  def __str__(self):
    return "?"

class ZombieTurtleRight(Tile, 1):
  def __str__(self):
    return "?"

class ZombieTurtleDown(Tile, 2):
  def __str__(self):
    return "?"

class ZombieTurtleLeft(Tile, 3):
  def __str__(self):
    return "?"

class Exit(Tile):
  def __str__(self):
    return "X"

class Floor(Tile):
  def __str__(self):
    return "F"

class Barrier(Tile):
  def __str__(self):
    return "B"

class Leash(Tile):
    def __str__(self):
      return "L"

class Spider(Tile):
    def __str__(self):
      return "S"

class SmallSpider(Tile):
  def __str__(self):
    return "s"

class Snake(Tile):
  def __str__(self):
    return "W"

class Health(Tile):
  def __str__(self):
    return "H"

class KingSpider(Tile):
  def __str__(self):
    return "K"

class Chest(Tile):
  def __str__(self):
    return "C"

class Coin(Tile):
  def __str__(self):
    return "c"

class Potion(Tile):
  def __str__(self):
    return "P"

class Vampire(Tile):
  def __str__(self):
    return "V"

class RedSpider(Tile):
  def __str__(self):
    return "R"

tile_map = {
  'U' : Player,
  'X' : Exit,
  'F' : Floor,
  'f' : Floor,
  'B' : Barrier,
  'L' : Leash,
  'S' : Spider,
  'R' : RedSpider,
  'V' : Vampire,
  'W' : Snake,
  'H' : Health,
  'K' : KingSpider,
  'C' : Chest,
  'c' : Coin,
  'P' : Potion,
  's' : SmallSpider,
  '8' : TurtleUp,
  '6' : TurtleRight,
  '2' : TurtleDown,
  '4' : TurtleLeft,
}