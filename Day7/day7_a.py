import re

puzzle_input = open("./puzzle_input.txt", "r").read()

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = dict()
        self.files = []
    
    def __str__(self):
        subdirnames=list(self.subdirs.keys())
        filenames=[f.name for f in self.files]
        parentname = self.parent.name if self.parent else None
        return f'{type(self).__name__}(name={self.name}, parent={parentname} subdirs={subdirnames}, files={filenames})'
        
    def total_size(self):
        size = 0
        for d in self.subdirs.values():
            size += d.total_size()
        size += sum([f.size for f in self.files])
        
        return size

def parse(input):
    lines = input.split('\n')
    home_dir = Directory('/', None)
    
    cdhome_pattern = re.compile("\$ cd \/")
    cd_pattern = re.compile("\$ cd ([A-Za-z]+)") 
    cdup_pattern = re.compile("\$ cd \.\.") 
    ls_pattern = re.compile("\$ ls")
    listing_dir = re.compile("dir ([A-Za-z]+)")
    listing_file = re.compile("(\d+) ([A-Za-z\.]+)")
    
    for l in lines:
        if cdhome_pattern.match(l):
            current_dir = home_dir
        elif cdup_pattern.match(l):
            current_dir = current_dir.parent
        elif cd_pattern.match(l):
            subdir_name = re.search("\$ cd ([A-Za-z]+)", l).group(1)
            current_dir = current_dir.subdirs[subdir_name]
        elif ls_pattern.match(l):
            pass
        elif listing_dir.match(l):
            subdir_name = listing_dir.search(l).group(1)
            current_dir.subdirs[subdir_name] = Directory(subdir_name, current_dir)            
        elif listing_file.match(l):
            size = int(listing_file.search(l).group(1))
            name = listing_file.search(l).group(2)
            current_dir.files.append(File(name, size))
    return home_dir

def draw_directory_structure(directory, indentation=0):
    print(" "*indentation, f"- {directory.name} (dir, total_size={directory.total_size()})")
    for subdir in directory.subdirs.values():
        draw_directory_structure(subdir, indentation+1)
    for file in directory.files:
        print(" "*(indentation+1), f"- {file.name} (file, size={file.size})")

def total_size_of_small_directories(directory):
    def collect_small_directories(current_dir):
        small_directories = []
        if current_dir.total_size() < 100000:
            small_directories.append(current_dir)
        for subdir in current_dir.subdirs.values():
            small_directories.extend(collect_small_directories(subdir))
        return small_directories
    
    return sum([d.total_size() for d in collect_small_directories(directory)])

#draw_directory_structure(parse(puzzle_input))
print(total_size_of_small_directories(parse(puzzle_input)))