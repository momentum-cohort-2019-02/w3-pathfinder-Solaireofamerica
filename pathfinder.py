from PIL import Image, ImageColor


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

    def draw_the_map(self):
        self.length_of_y_axis = []
        for y in range(len(self.the_map.elevations)):
            for x in range(len(self.the_map.elevations)):
                rgb_value = self.the_map.get_intensity(x, y)
                self.map_img.putpixel((x, y), (rgb_value, rgb_value, rgb_value))
                self.length_of_y_axis.append(1)
        self.map_img.save('map_img.png', "PNG")
        return self.length_of_y_axis

    def draw_path(self, path, image, rgb):
        for path_point in path:
            image.putpixel(path_point, rgb)
        self.map_img.save('map_img1.png', "PNG")



class Pathfinder:

    def __init__(self, the_map):
        self.the_map = the_map

    def point_finder(self, current_x, current_y):
        point_list = []
        while current_x < len(self.the_map.elevations[0]) - 1:
            possible_ys = [current_y]
            if current_y - 1 >= 0:
                possible_ys.append(current_y - 1)
            if current_y + 1 < len(self.the_map.elevations):
                possible_ys.append(current_y + 1)

            diffs = [abs(self.the_map.elevations[poss_y][current_x + 1] - self.the_map.elevations[current_y][current_x]) for poss_y in possible_ys]

            min_diff = min(diffs)
            min_diff_index = diffs.index(min_diff)
            next_y = possible_ys[min_diff_index]

            current_x += 1
            current_y = next_y
            point_list.append((current_x, current_y))
        return point_list

    def path_finder(self, y):
        path_1 = self.point_finder(0, y)
        return path_1
    

if __name__ == "__main__":
    main_map = ElevationMap('elevation_large.txt')
    drawing_tool = DrawMap(main_map)
    pfinder = Pathfinder(main_map)
    drawing_tool.draw_the_map()
    path_list = []
    for y in range(len(main_map.elevations[0])):
        path_list.append(pfinder.path_finder(y))
        
    for path in path_list:
        drawing_tool.draw_path(path, drawing_tool.map_img, (240, 0, 0))
