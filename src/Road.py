from random import choice 

# Road sections will be defined as 8x8 matrices, where the road is composed of road sections
STRAIGHT_ROAD = [[0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0]]

ROAD_BEND     = [[0, 0, 0, 0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0]]

CROSSROAD     = [[0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0]]

T_JUNCTION    = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0]]

CHICANE       = [[0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 1, 1, 1, 1, 0, 0]]


GRASS         = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

class ROAD_ENUM:
    straight    = STRAIGHT_ROAD,
    bend        = ROAD_BEND,
    crossroad   = CROSSROAD,
    t_junction  = T_JUNCTION,
    chicane     = CHICANE,
    grass       = GRASS

class ROAD_DIRECTIONS:
    LEFT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3

class Road:
    road = [[GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
            [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS]]

    section_map = [STRAIGHT_ROAD, ROAD_BEND, CHICANE, CROSSROAD, T_JUNCTION]
    current_rotation = ROAD_DIRECTIONS.LEFT

    # We'll need a function to rotate roads by 90 degrees
    @staticmethod
    def rotate_by_90(matrix: list) -> list:
        matrix_x, matrix_y = 8, 8
        
        transposition = [[matrix[x][y] for x in range(matrix_x)]  for y in range(matrix_y)]
        rotation = [[row[x] for x in range(matrix_x - 1, -1, -1)] for row in transposition]

        return rotation

    # For standard, the origin is 0, 0
    def __init__(self, origin_x: int = 0, origin_y: int = 0) -> None:
        straight_section = self.rotate_by_90(self.rotate_by_90(STRAIGHT_ROAD))
        self.road[origin_x][origin_y] = straight_section

    def get_roads(self):
        first_normalisation = [i for road in self.road for i in road]
        second_normalisation = [i for road in first_normalisation for i in road]
        return second_normalisation

    # We need rules
    # A chunk is just a Xx8 set of sections
    # !IMPORTANT! instead of rotating road sections we can rotate the entire board for generation
    # A rotation of the board by +90 degrees is just the same as rotating sections by -90 degrees
    def generate_chunk(self, x: int = 0) -> None:
        edge_ruleset = False
        if x in (0, 7):
            # Cannot use crossroads nor junctions unless x is 1 through 6
            edge_ruleset = True
    
        # How should rotation work?
        # Only straight sections, t-junctions and bends require rotation
        # Keep track of current rotation and build along that
        for i, j in enumerate(self.road[x]):
            # match self.current_rotation:
            #     case ROAD_DIRECTIONS.LEFT:
            #         # If the current orientation is left-facing, since all road sections are left-facing by default
            #         # nothing needs to be done
            #         break
            #     case ROAD_DIRECTIONS.UP:
            #         # This requires a self-rotation of one
            #         self.road = self.rotate_by_90(self.road)
            #         break
            #     case ROAD_DIRECTIONS.DOWN:
            #         # This requires a self-rotation of two
            #         self.road = self.rotate_by_90(self.rotate_by_90(self.road))
            #         break
            #     case ROAD_DIRECTIONS.RIGHT:
            #         # This requires a self-rotation of three
            #         self.road = self.rotate_by_90(self.rotate_by_90(self.rotate_by_90(self.road)))
            #         break

            # We only need to rotate when a turn happens which can be given by a crossroad, t-junction or bend
            rotate = False
            next_road_piece = choice(self.section_map[:3] if edge_ruleset else self.section_map)
            if (next_road_piece in (ROAD_BEND, T_JUNCTION, CROSSROAD)):
                # This will require a rotation afterwards
                rotate = True

            self.road[x][i] = next_road_piece
            if (rotate):
                self.road = self.rotate_by_90(self.road)