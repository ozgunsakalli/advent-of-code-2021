

from collections import Counter


test_data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

# test_data = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc"""


test_data1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_data = test_data.split('\n')
test_data1 = test_data1.split('\n')


class Path():

    def __init__(self, parent, cave_map, path=['start']):
        self.parent = parent
        self.cave_map = cave_map
        self.path = path
        self.parent.append(self)
    

    def find_paths(self):
        
        start_point = self.path[-1]

        self.check_visits()

        split_links = [link.split('-') for link in self.cave_map.copy()]
        relevant_links = [link for link in split_links if start_point in link]
    
        for link in relevant_links:
            print('link:', link)

            new_path = self.extend_path(link, start_point)

            if new_path[-1] == 'end':
                cave_map = None
            else:
                cave_map = self.cave_map

            if start_point == 'start':
                cave_map = [link for link in cave_map()
                            if 'start' not in link]

            if self in self.parent:
                self.parent.remove(self)
            # print(new_path)
            Path(self.parent, cave_map, new_path)


    def extend_path(self, link, start_point):

        # print('link:', link)
        # print('start_point:', start_point)
        link.remove(start_point)
        # print('new_point:', new_point)
        new_point = link[0]

        new_path = self.path.copy()
        new_path.append(new_point)

        return new_path


    def check_visits(self):

        lower_points = [point for point in self.path if point.islower()]
        lower_points = Counter(lower_points)

        double_visit = None
        for point, count in lower_points.items():
            if count == 2:
                double_visit = point
        
        if double_visit:
            for link in self.cave_map.copy():
                p1, p2 = link.split('-')

                if lower_points[p1] >=1 or lower_points[p2] >= 1:
                    self.cave_map.remove(link)


paths = []
a = Path(paths, test_data1)