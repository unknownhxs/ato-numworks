import kandinsky as k
import ion as i
import time as t

SCREEN_W = 320
SCREEN_H = 240
TS = 16
W = SCREEN_W // TS
H = SCREEN_H // TS
PS = 16
SPD = 5
MAP_MAX_W = 500
MAP_MAX_H = 500
BORDER_SIZE = 10
HALF_W = SCREEN_W // 2
HALF_H = SCREEN_H // 2

P = {
    'G': (85, 139, 85), 'GL': (100, 160, 100), 'GD': (70, 120, 70),
    'P': (222, 184, 135), 'TT': (34, 139, 34), 'TR': (101, 67, 33),
    'R': (178, 34, 34), 'RD': (139, 0, 0), 'RL': (220, 50, 50),
    'W': (160, 82, 45), 'WL': (180, 100, 60), 'WD': (140, 70, 35),
    'D': (101, 67, 33), 'DD': (70, 45, 20), 'WIN': (135, 206, 250),
    'WID': (70, 130, 180), 'C': (80, 80, 80), 'CD': (50, 50, 50),
    'F': (138, 43, 226), 'ROCK': (105, 105, 105), 'ROD': (64, 64, 64),
    'B': (0, 100, 0), 'BL': (0, 0, 0), 'WH': (255, 255, 255),
    'BR': (139, 69, 19),
    'BLUE': (0, 100, 255),
    'SLIME': (50, 100, 200),
    'SLIME_D': (30, 60, 150),
    'SLIME_L': (100, 150, 255)
}

def c(n): return k.color(*P[n])

T_GRASS, T_PATH, T_TREE, T_ROCK, T_BUSH, T_FLOWER, T_HOUSE, T_BORDER = 0, 1, 2, 3, 4, 5, 6, 7

COLORS = {k: c(k) for k in P}

def get_tile_at_world(wx, wy):
    if wx < 0 or wy < 0 or wx >= MAP_MAX_W or wy >= MAP_MAX_H:
        return None
    if wx < BORDER_SIZE or wy < BORDER_SIZE or wx >= MAP_MAX_W - BORDER_SIZE or wy >= MAP_MAX_H - BORDER_SIZE:
        return T_BORDER
    tx = wx // TS
    ty = wy // TS
    seed = (tx * 73856093) ^ (ty * 19349663)
    seed = (seed * 1103515245 + 12345) & 0x7FFFFFFF
    rand = seed % 100
    if rand < 5:
        return T_TREE
    elif rand < 10:
        return T_ROCK
    return T_GRASS

def draw_tile_screen(sx, sy, tile_type, wx=0, wy=0):
    if tile_type == T_GRASS:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        if (sx + sy) & 0x20 == 0:
            k.fill_rect(sx + 4, sy + 4, 4, 4, COLORS['GL'])
    elif tile_type == T_PATH:
        k.fill_rect(sx, sy, TS, TS, COLORS['P'])
        k.fill_rect(sx, sy, TS, 2, COLORS['DD'])
    elif tile_type == T_TREE:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        k.fill_rect(sx + 4, sy, 8, 8, COLORS['TT'])
        k.fill_rect(sx + 6, sy + 8, 4, 6, COLORS['TR'])
    elif tile_type == T_ROCK:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        k.fill_rect(sx + 4, sy + 4, 8, 6, COLORS['ROCK'])
        k.fill_rect(sx + 8, sy + 6, 4, 4, COLORS['ROD'])
    elif tile_type == T_BUSH:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        k.fill_rect(sx + 3, sy + 4, 10, 8, COLORS['B'])
        k.fill_rect(sx + 2, sy + 6, 12, 6, COLORS['B'])
    elif tile_type == T_FLOWER:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        k.fill_rect(sx + 6, sy + 6, 4, 4, COLORS['F'])
    elif tile_type == T_HOUSE:
        k.fill_rect(sx, sy, TS, TS, COLORS['G'])
        k.fill_rect(sx + 2, sy + 6, 12, 10, COLORS['W'])
        for i in range(0, 12, 4):
            k.fill_rect(sx + 2 + i, sy + 6, 1, 10, COLORS['WD'])
        k.fill_rect(sx, sy + 4, 16, 4, COLORS['R'])
        k.fill_rect(sx + 6, sy + 12, 4, 4, COLORS['D'])
    elif tile_type == T_BORDER:
        is_left = wx < BORDER_SIZE
        is_right = wx >= MAP_MAX_W - BORDER_SIZE
        is_top = wy < BORDER_SIZE
        is_bottom = wy >= MAP_MAX_H - BORDER_SIZE
        if is_left:
            color_idx = wx % (BORDER_SIZE * 2)
            color = COLORS['BLUE'] if color_idx < BORDER_SIZE else COLORS['WH']
            k.fill_rect(sx, sy, TS, TS, color)
        elif is_right:
            color_idx = (MAP_MAX_W - wx - 1) % (BORDER_SIZE * 2)
            color = COLORS['BLUE'] if color_idx < BORDER_SIZE else COLORS['WH']
            k.fill_rect(sx, sy, TS, TS, color)
        elif is_top:
            color_idx = wy % (BORDER_SIZE * 2)
            color = COLORS['BLUE'] if color_idx < BORDER_SIZE else COLORS['WH']
            k.fill_rect(sx, sy, TS, TS, color)
        elif is_bottom:
            color_idx = (MAP_MAX_H - wy - 1) % (BORDER_SIZE * 2)
            color = COLORS['BLUE'] if color_idx < BORDER_SIZE else COLORS['WH']
            k.fill_rect(sx, sy, TS, TS, color)
        else:
            k.fill_rect(sx, sy, TS, TS, COLORS['G'])

def draw_world(cam_x, cam_y):
    k.fill_rect(0, 0, SCREEN_W, SCREEN_H, COLORS['BL'])
    start_tx = (cam_x - HALF_W) // TS - 1
    start_ty = (cam_y - HALF_H) // TS - 1
    end_tx = (cam_x + HALF_W) // TS + 2
    end_ty = (cam_y + HALF_H) // TS + 2
    for ty in range(start_ty, end_ty):
        wy = ty * TS
        sy = wy - cam_y + HALF_H
        if -TS <= sy < SCREEN_H + TS:
            for tx in range(start_tx, end_tx):
                wx = tx * TS
                sx = wx - cam_x + HALF_W
                if -TS <= sx < SCREEN_W + TS:
                    tile = get_tile_at_world(wx, wy)
                    if tile is not None:
                        draw_tile_screen(sx, sy, tile, wx, wy)
                    else:
                        k.fill_rect(sx, sy, TS, TS, COLORS['BL'])

def draw_player(frame=0):
    sx = HALF_W - PS // 2
    sy = HALF_H - PS // 2
    squash = 1 if frame else 0
    k.fill_rect(sx + 2, sy + 2 + squash, 12, 10 - squash * 2, COLORS['SLIME'])
    k.fill_rect(sx + 3, sy + 3 + squash, 10, 8 - squash * 2, COLORS['SLIME'])
    k.fill_rect(sx + 4, sy + 4 + squash, 8, 6 - squash * 2, COLORS['SLIME_L'])
    k.fill_rect(sx + 4, sy + 3 + squash, 5, 4, COLORS['SLIME_L'])
    k.fill_rect(sx + 5, sy + 4 + squash, 3, 3, COLORS['SLIME_L'])
    k.fill_rect(sx + 6, sy + 5 + squash, 1, 2, COLORS['WH'])
    k.fill_rect(sx + 3, sy + 11 - squash, 10, 2, COLORS['SLIME_D'])
    k.fill_rect(sx + 4, sy + 12 - squash, 8, 1, COLORS['SLIME_D'])
    k.fill_rect(sx + 1, sy + 4 + squash, 1, 2, COLORS['SLIME'])
    k.fill_rect(sx + 14, sy + 4 + squash, 1, 2, COLORS['SLIME'])
    k.fill_rect(sx + 2, sy + 3 + squash, 1, 1, COLORS['SLIME'])
    k.fill_rect(sx + 13, sy + 3 + squash, 1, 1, COLORS['SLIME'])

def handle_input(wx, wy):
    nwx, nwy, m = wx, wy, False
    if i.keydown(i.KEY_UP):
        if nwy - SPD >= 0:
            nwy -= SPD
            m = True
    elif i.keydown(i.KEY_DOWN):
        if nwy + SPD + PS <= MAP_MAX_H:
            nwy += SPD
            m = True
    if i.keydown(i.KEY_LEFT):
        if nwx - SPD >= 0:
            nwx -= SPD
            m = True
    elif i.keydown(i.KEY_RIGHT):
        if nwx + SPD + PS <= MAP_MAX_W:
            nwx += SPD
            m = True
    return nwx, nwy, m

def loading_screen():
    k.fill_rect(0, 0, SCREEN_W, SCREEN_H, COLORS['BL'])
    k.draw_string("Chargement...", HALF_W - 50, HALF_H - 10, COLORS['WH'], COLORS['BL'])
    for i in range(3):
        k.fill_rect(HALF_W - 30 + i * 20, HALF_H + 10, 15, 15, COLORS['BLUE'])
        t.sleep(0.1)
    t.sleep(0.2)

def game_engine():
    loading_screen()
    world_x = MAP_MAX_W // 2
    world_y = MAP_MAX_H // 2
    anim_frame = 0
    last_frame = -1
    fps_counter = 0
    fps = 0
    fps_timer = t.monotonic()
    draw_world(world_x, world_y)
    draw_player(anim_frame)
    while True:
        if i.keydown(i.KEY_ZERO):
            break
        t.sleep(0.02)
        nwx, nwy, moved = handle_input(world_x, world_y)
        if moved:
            world_x, world_y = nwx, nwy
            draw_world(world_x, world_y)
            anim_frame = 1 - anim_frame
            draw_player(anim_frame)
            last_frame = anim_frame
        elif anim_frame != last_frame:
            draw_player(anim_frame)
            last_frame = anim_frame
        fps_counter += 1
        current_time = t.monotonic()
        if current_time - fps_timer >= 1.0:
            fps = fps_counter
            print("FPS:", fps)
            fps_counter = 0
            fps_timer = current_time

game_engine()
