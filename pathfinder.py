# import pillow
# take the list of lists and make a dictionary where the key is and int and the key the value is a tuple containing
# the x,y point
# the large list are the rows and the smaller list items are the columns

# need to open the image and format the text inside. .split will return all of the numbers, individually as a list. 
# img_file = open("elevation_small.txt")
# lowest point is 3139
# elevations = []
# with open("elevation_small.txt", "r") as img_file:
#     main_list = [line.split() for line in img_file]
#     x = 0
    # dict((elevation, x + 1) for elevations in main_list)
    # ele_dict = {el: 0 for el in main_list[0:][0:]}
    # for i in main_list:
    #     small_list = main_list.append(i)


class ElevationMap:

    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.split()])


        # max_elevations = []
        # for row in self.elevations:
        #     max_elevations.append(max(row))
        # self.max_elevations = max(max_elevations)

        self.max_elevation = max(max(row) for row in self.elevations)
        self.min_elevation = min(min(row) for row in self.elevations)
    def ele_print(self, max_elevation, min_elevation):
        print(min_elevation)
    def get_elevation(self, x, y):
        return self.elevations[y][x]

    def get_intensity(self, x, y):
        return (self.get_elevation(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255
 

 # class for map from text file. 
 # function in map class i.e. for intensity
 # class that draws the map. 
 # class for pathfinding. list of position 
 # total elevation change as a tuple or method to find the lowest change in elevation

# Then we can format that list into a tuple with nested dictionaries where the number from the file is the key and
# the coordinating points on the graph are the value. we probably also need to separate the file line by line. 


if __name__ == "__main__":
    pass