import random
import pygame
import sys
from pygame.locals import *

FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
REVEAL_SPEED = 8
BOX_SIZE = 40
GAP_SIZE = 10       # size between boxes
BOARD_WIDTH = 10    # number of columns of icons
BOARD_HEIGHT = 7    # number of rows of icons
assert (BOARD_WIDTH * BOARD_HEIGHT) % 2 == 0, 'Board needs pair boxes.'
X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * (BOX_SIZE + GAP_SIZE))) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - (BOARD_HEIGHT * (BOX_SIZE + GAP_SIZE))) / 2)

# Colors     R   G   B
GRAY = (100, 100, 100)
NAVY_BLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BG_COLOR = NAVY_BLUE
LIGHT_BG_COLOR = GRAY
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALL_COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, GRAY)
ALL_SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALL_COLORS) * len(ALL_SHAPES) * 2 >= BOARD_WIDTH * BOARD_HEIGHT,\
    'Board is too small for the number of shapes/colors defined.'


def main():
    global FPS_CLOCK, DISPLAY_SURF
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    mouse_x = 0  # to store x coordinate of mouse event
    mouse_y = 0  # to store y...
    pygame.display.set_caption('Memory Game')

    main_board = get_randomized_board()
    revealed_boxes = generate_revealed_boxes_data(False)

    first_selection = None  # stores the x,y of the first box clicked

    DISPLAY_SURF.fill(BG_COLOR)
    start_game_animation(main_board)

    # main game loop
    while True:
        mouse_clicked = False

        DISPLAY_SURF.fill(BG_COLOR)
        draw_board(main_board, revealed_boxes)

        # event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouse_clicked = True

        # two int represent XY board coordinates of the box that the mouse is over
        box_x, box_y = get_box_at_pixel(mouse_x, mouse_y)
        if box_x is not None and box_y is not None:
            # mouse is currently over a box
            if not revealed_boxes[box_x][box_y]:  # if it's false, box is covered
                draw_highlight_box(box_x, box_y)
            if not revealed_boxes[box_x][box_y] and mouse_clicked:
                reveal_boxes_animation(main_board, [(box_x, box_y)])
                revealed_boxes[box_x][box_y] = True  # set the box as 'revealed'
                if first_selection is None:  # current box was the first box clicked
                    first_selection = (box_x, box_y)
                else:  # current box was the second box clicked
                    icon1shape, icon1color = get_shape_and_color(main_board, first_selection[0], first_selection[1])
                    icon2shape, icon2color = get_shape_and_color(main_board, box_x, box_y)
                    if icon1shape != icon2shape or icon1color != icon2color:
                        # icons don't match, re-cover up both selections
                        pygame.time.wait(100)  # 1000 ms
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]), (box_x, box_y)])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[box_x][box_y] = False
                    elif has_won(revealed_boxes):  # check if all pairs found
                        game_won_animation(main_board)
                        pygame.time.wait(2000)

                        # reset the board
                        main_board = get_randomized_board()
                        revealed_boxes = generate_revealed_boxes_data(False)

                        # show the fully unrevealed board
                        draw_board(main_board, revealed_boxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # replay game start animation
                        start_game_animation(main_board)
                    first_selection = None  # reset first selection variable
        # redraw screen and wait clock tick
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


# functions
def generate_revealed_boxes_data(val):
    revealed_boxes = []
    for i in range(BOARD_WIDTH):
        revealed_boxes.append([val] * BOARD_HEIGHT)
    return revealed_boxes


def get_randomized_board():
    # get a list of every possible shape in every possible color
    icons = []
    for color_ in ALL_COLORS:
        for shape in ALL_SHAPES:
            icons.append((shape, color_))
    random.shuffle(icons)  # randomize order of icons list
    num_icons_used = int(BOARD_WIDTH * BOARD_HEIGHT / 2)  # calculate how many icos are needed
    icons = icons[:num_icons_used]*2  # make a pair of each
    random.shuffle(icons)

    # create the board data structure, with randomly placed icons
    board = []
    for x in range(BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(icons[0])
            del icons[0]  # remove icons as we assign them
        board.append(column)
    return board


def split_into_groups_of(group_size, the_list):
    # splits a list into a list of lists, where the inner lists
    # have at most group_size number of items
    result = []
    for i in range(0, len(the_list), group_size):
        result.append(the_list[i:i + group_size])
    return result


def left_top_coordinates_of_box(box_x, box_y):
    # convert board coord to pixel coord
    left = box_x * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    top = box_y * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return left, top


def get_box_at_pixel(x, y):
    for box_x in range(BOARD_WIDTH):
        for box_y in range(BOARD_HEIGHT):
            left, top = left_top_coordinates_of_box(box_x, box_y)
            box_rect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if box_rect.collidepoint(x, y):
                return box_x, box_y
    return None, None


def draw_icon(shape, color_, box_x, box_y):
    quarter = int(BOX_SIZE * 0.25)
    half = int(BOX_SIZE * 0.5)
    left, top = left_top_coordinates_of_box(box_x, box_y)  # get pixel coord
    # draw shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAY_SURF, color_, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAY_SURF, BG_COLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAY_SURF, color_, (left + quarter, top + quarter, BOX_SIZE - half, BOX_SIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAY_SURF, color_, ((left + half, top), (left + BOX_SIZE - 1, top + half),
                                                   (left + half, top + BOX_SIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(DISPLAY_SURF, color_, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAY_SURF, color_, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAY_SURF, color_, (left, top + quarter, BOX_SIZE, half))


def get_shape_and_color(board, box_x, box_y):
    # shape value for x,y spot is stored in board[x][y][0]
    # color value for x,y spot is stored in board[x][y][1]
    return board[box_x][box_y][0], board[box_x][box_y][1]


def draw_box_covers(board, boxes, coverage):
    # draws boxes being covered/revealed
    # @boxes is a list of 2 items (x,y of box)
    for box in boxes:
        left, top = left_top_coordinates_of_box(box[0], box[1])
        pygame.draw.rect(DISPLAY_SURF, BG_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
        shape, color_ = get_shape_and_color(board, box[0], box[1])
        draw_icon(shape, color_, box[0], box[1])
        if coverage > 0:  # only draw cover if there is an coverage
            pygame.draw.rect(DISPLAY_SURF, BOX_COLOR, (left, top, coverage, BOX_SIZE))
    pygame.display.update()
    FPS_CLOCK.tick(FPS)


def reveal_boxes_animation(board, boxes_to_reveal):
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, - REVEAL_SPEED):
        draw_box_covers(board, boxes_to_reveal, coverage)


def cover_boxes_animation(board, boxes_to_cover):
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        draw_box_covers(board, boxes_to_cover, coverage)


def draw_board(board, revealed):
    for box_x in range(BOARD_WIDTH):
        for box_y in range(BOARD_HEIGHT):
            left, top = left_top_coordinates_of_box(box_x, box_y)
            if not revealed[box_x][box_y]:
                # draw a covered box
                pygame.draw.rect(DISPLAY_SURF, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                # draw revealed icon
                shape, color_ = get_shape_and_color(board, box_x, box_y)
                draw_icon(shape, color_, box_x, box_y)


def draw_highlight_box(box_x, box_y):
    left, top = left_top_coordinates_of_box(box_x, box_y)
    pygame.draw.rect(DISPLAY_SURF, HIGHLIGHT_COLOR, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10), 4)


def start_game_animation(board):
    # randomly reveal the boxes 8 at a a time
    covered_boxes = generate_revealed_boxes_data(False)
    boxes = []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    box_groups = split_into_groups_of(8, boxes)
    draw_board(board, covered_boxes)
    for boxGroup in box_groups:
        reveal_boxes_animation(board, boxGroup)
        cover_boxes_animation(board, boxGroup)


def game_won_animation(board):
    # flash bg color
    covered_boxes = generate_revealed_boxes_data(True)
    color1 = LIGHT_BG_COLOR
    color2 = BG_COLOR
    for i in range(13):
        color1, color2 = color2, color1  # swap colors
        DISPLAY_SURF.fill(color1)
        draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)


def has_won(revealed_boxes):
    for i in revealed_boxes:
        if False in i:
            return False
    return True  # returns True if all boxes have been revealed


if __name__ == '__main__':
    main()
