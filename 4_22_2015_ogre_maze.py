"""
http://www.reddit.com/r/dailyprogrammer/comments/33hwwf/20150422_challenge_211_intermediate_ogre_maze/
"""

class Maze(object):
    def __init__(self, maze):
        self.incomplete = self.build_maze(maze)
        self.ogre_start = self.find_ogre() # [ [top left], [top right], [bottom left], [bottom right] ] 
        self.complete   = []

    def build_maze(self, input_string):
        return [ [ input_string[x][y] for x in range(0, len(input_string)) ] for y in range(0, len(input_string[0])) ]
        # self.ogre_start = self.find_ogre()

    def print_maze(self, maze):
        for y in range(0, len(maze[0])):
            for x in range(0,len(maze)):
                print(maze[x][y], end=' ')
                # print('x:' + str(x) + '  y:' + str(y)) # Debugging
            print()

    def find_ogre(self):
        for y in range(0, len(self.incomplete[0])):
            for x in range(0,len(self.incomplete)):
                if self.incomplete[x][y] == '@':
                    return [ [x,y], [x+1,y], [x,y+1], [x+1,y+1] ]
        return [-1]

if __name__ == "__main__":
    test_maze = Maze([ '..........',
                       '..........',
                       '..O@@O....',
                       '...@@.....',
                       '...OO.....',
                       '.....OO...',
                       '.........$' ])
    test_maze.print_maze(test_maze.incomplete)