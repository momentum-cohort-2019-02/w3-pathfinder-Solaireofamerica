from PIL import Image, ImageDraw, ImageColor
# take the list of lists and make a dictionary where the key is and int and the key the value is a tuple containing
# the x,y point
# the large list are the rows and the smaller list items are the columns

# need to open the image and format the text inside. .split will return all of the numbers, individually as a list. 
# img_file = open("elevation_small.txt")
# lowest point is 3139


class ElevationMap:

    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])

        self.max_elevation = max(max(row) for row in self.elevations)
        self.min_elevation = min(min(row) for row in self.elevations)

    def get_elevation(self, x, y):
        return self.elevations[y][x]


    def get_intensity(self, x, y):
        return int((self.get_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)

 
class DrawMap:

    def __init__(self, the_map):
        self.the_map = the_map
        self.map_img = Image.new('RGB', (len(self.the_map.elevations), len(self.the_map.elevations[0])), (255,255,255))

    def do_the_draw(self):
        for y in range(len(self.the_map.elevations)):
            for x in range(len(self.the_map.elevations)):
                rgb_value = self.the_map.get_intensity(x, y)
                self.map_img.putpixel((x, y), (rgb_value, rgb_value, rgb_value))
        self.map_img.save('map_img.jpg', "JPEG")


# class Pathfinder:
# pathfinder class will find the paths. need to find out how to do it lol
# not sure if I need to draw the paths in pathfinder or DrawMap 


cur_x = 0
cur_y = 0
# import math
while cur_x < len(elevations[0]) - 1:
    possible_ys = []
    if cur_y - 1 >= 0:
        possible_ys.append(cur_y - 1)
    if cur_y + 1 < len(elevations):
        possible_ys.append(cur_y + 1)

    diffs = [
        abs(elevations[poss_y][cur_x + 1]elevations[cur_y][cur_x]) 
        for poss_y in possible_ys
    ]

    min_diff = min(diffs)
    min_diff_index = diffs.index(min_diff)
    next_y = possible_ys[min_diff_index]

    cur_x += 1
    cur_y = next_y

# class for map from text file. 
# function in map class i.e. for intensity
# class that draws the map. 
# class for pathfinding. list of position 
# total elevation change as a tuple or method to find the lowest change in elevation

# Then we can format that list into a tuple with nested dictionaries where the number from the file is the key and
# the coordinating points on the graph are the value. we probably also need to separate the file line by line. 


if __name__ == "__main__":
    main_map = ElevationMap('elevation_small.txt')
    drawing_tool = DrawMap(main_map)
    drawing_tool.do_the_draw()