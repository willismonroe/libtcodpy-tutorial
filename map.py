import libtcodpy as libtcod # for field of view management

class Map(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.objects = []

        # TODO: do stairs get cloned when saved?
        self.stairs = None
        self.fov_map = None

        # Maps default to blocked & unexplored
        self.blocked = [[ True for y in range(height) ] for x in range(width) ]
        self.explored = [[ False for y in range(height) ] for x in range(width) ]
        self.block_sight = [[ True for y in range(height) ] for x in range(width) ]

    def initialize_fov(self):
        # After being loaded from savegame, we need to make sure the C state
        # is reinitialized, so we can't just set this in __init__().
        self.fov_needs_recompute = True
        self.fov_map = libtcod.map_new(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                libtcod.map_set_properties(self.fov_map, x, y, not self.block_sight[x][y], not self.blocked[x][y])
