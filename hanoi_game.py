#################################################################
# WEB PAGES I'VE USED: https://en.wikipedia.org/wiki/Tower_of_Hanoi
#################################################################

from typing import Any


def play_hanoi_helper(hanoi: Any, n: int, src: Any, dest: Any,
                      temp: Any) -> None:
    """A function that plays the 'Hanoi Towers' game!"""
    # If you want to move 0 discs or fewer, the board should not change
    if n > 1:
        if n == 1:
            # If n = 1, that means you only have 1 disc left to move,
            # so move it from the source to the destination
            hanoi.move(src, dest)
        else:
            # Move n-1 discs from the source to the temp tower
            play_hanoi_helper(hanoi, n - 1, src, temp, dest)
            # Move the current disc from the source tower
            # to the destination tower
            hanoi.move(src, dest)
            # Move the n-1 discs that we have just placed on the temp tower,
            # from the temp tower to the dest tower
            play_hanoi_helper(hanoi, n - 1, temp, dest, src)


def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any) -> None:
    """
    A function that plays the hanoi towers game,
    using the algorithm provided in https://en.wikipedia.org/wiki/Tower_of_Hanoi
    """
    # If n equals 1, that means there is only one disc to move,
    # so move it to the destination tower
    if n == 1:
        hanoi.move(src, dest)
    else:
        # For some reason, which is unclear to me, if I don't increment n by 1,
        # the function plays the game as if I called it with n-1,
        # so if I increment n by 1, the function plays the game
        # as if I called it with n+1-1, which is n
        play_hanoi_helper(hanoi, n + 1, src, dest, temp)
