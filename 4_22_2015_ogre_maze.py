"""
http://www.reddit.com/r/dailyprogrammer/comments/33hwwf/20150422_challenge_211_intermediate_ogre_maze/
"""
def create_maze(input_string):
    maze = [ [ input_string[x][y] for x in range(len(input_string[0])) ] for y in range(len(input_string)) ]

if __name__ == "__main__":
    test_maze = [ '@@........',
                  '@@O.......',
                  '.....O.O..',
                  '..........',
                  '..O.O.....',
                  '..O....O.O',
                  '.O........',
                  '..........',
                  '.....OO...',
                  '.........$' ]
    
    maze = create_maze(test_maze)
