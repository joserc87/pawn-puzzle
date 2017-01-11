import sys
from pawn import PurplePawn, RedPawn, BluePawn, OrangePawn, PinkPawn

class bcolors:
    WHITE = '\033[107m'
    BLACK = '\033[40m'
    LIGHT_GRAY = '\033[48;5;250m'
    GRAY = '\033[48;5;240m'
    DARK_GRAY = '\033[48;5;235m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class fcolors:
    PURPLE = '\033[35m'
    ENDC = '\033[39m'

def print_board(height, width, skulls, solution):

    # Colors:
    light_tile_color = bcolors.LIGHT_GRAY
    dark_tile_color = bcolors.DARK_GRAY
    border_color = bcolors.GRAY

    print('\n ' + border_color + ' '*(3*width + 2*2) + bcolors.ENDC)
    for idxRow, row in enumerate(range(height)):
        sys.stdout.write(' ' + border_color + '  ' + bcolors.ENDC)
        for idxColumn, column in enumerate(range(width)):
            pos = (row, column)
            # Set the output background for the tile:
            if (row + column) % 2 == 0:
                sys.stdout.write(dark_tile_color)
            else:
                sys.stdout.write(light_tile_color)

            # Get the piece to print (or skull), if any
            piece = u' '
            if pos in skulls:
                # The unicode codepoint for the skull is 2620
                piece = fcolors.PURPLE + u'\u2620' + fcolors.ENDC
            else:
                for pawn, pawn_pos in solution:
                    if pos == pawn_pos:
                        piece = pawn.__repr__()
            # Print the piece
            sys.stdout.write(u' ' + piece + u' ')

        sys.stdout.write(border_color + '  ')
        sys.stdout.write(bcolors.ENDC + '\n')

    print(' ' + border_color + ' '*(3*width + 2*2) + bcolors.ENDC)
    sys.stdout.write('\n')
    sys.stdout.flush()

def solve(available_positions, uncovered_positions, pawns, skulls, find_all_solutions=False):
    """
    Solves the problem. It builds the coverage as it goes.
    Args:
        available_positions (list): A list of tuples (row, column) with the
            positions available for pawns.  This is, all the positions of
            the board, minus the skulls and the pawns already placed.
        uncovered_positions (list): A list of tuples with the available
            positions that are not covered (the placed pawns can't move to
            those positions).
        pawns (list): The Pawn objects to place
        skulls (list): A list of tuples with the positions of the pink
            skulls
        find_all_solutions (bool): When true, it tries to find all the
            solutions. Again, TRIES ;). When this is true, don't expect it to
            finish anytime soon, continue with your life. Maybe your grand
            grand children will see this end.


    Returns A list of solutions, where each solution is a list of tuples
        (Pawn, (row, column)), or an empty list if no solution was found.
    """

    solutions = []

    # If there are no more pawns to place, check the coverage
    if pawns == []:
        if len(uncovered_positions) == 0:
            # Array of solutions contains one item. This item will be
            # completed when returned
            if find_all_solutions:
                print('Found another solution')
            return [[]]
        else:
            # No solutions
            return []
    else:
        # The pawn to place
        pawn = pawns[0]
        for numPosition, position in enumerate(available_positions):
            pawn.set_pos(position)
            # Check that the pawn can't move to a skull
            if [skull for skull in skulls if pawn.can_move(skull)] == []:
                # Recursively, place the other pawns
                partial_solutions = solve(
                        available_positions[:numPosition] +
                            available_positions[numPosition + 1:],
                        [pos for pos in uncovered_positions
                            if not pawn.can_move(pos)],
                        pawns[1:],
                        skulls,
                        find_all_solutions)
                if len(partial_solutions) > 0:
                    # Add the position of the current pawn to the partial
                    # solutions:
                    solutions += [[(pawn, position)] + partial_solution for
                            partial_solution in partial_solutions]
                    if not find_all_solutions:
                        break

    return solutions

def main(height, width, pawns, skulls, verbose=False):
    # Enumerate all the positions, excep the occupied by the skulls
    positions = [(x, y) for x in range(width) for y in range(height) if (x, y) not in skulls]

    print('Placing pawns ' + ' '.join([pawn.__repr__() for pawn in pawns]) + ' in board')

    if verbose:
        print_board(height, width, skulls, [])

    solutions = solve(positions, positions, pawns, skulls)
    for solution in solutions:
        print_board(height, width, skulls, solution)

width = 8
height = 8
skulls = [
        (3, 1),
        (3, 4),
        (4, 1),
        (4, 4),
        (7, 4),
        (7, 6),
        (7, 7)
        ]

pawns = [PurplePawn(),
        RedPawn(),
        RedPawn(),
        BluePawn(),
        OrangePawn(),
        PinkPawn()
        ]

main(height, width, pawns, skulls)

