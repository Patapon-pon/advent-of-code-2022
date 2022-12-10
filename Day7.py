from typing import List


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
    
    def __repr__(self) -> str:
        return f"{self.size} {self.name}"

class Directory:

    def __init__(self, name) -> None:
        self.name = name
        self.child_directories: List[Directory] = []
        self.files: List[File] = []
    
    def size(self) -> int:
        total_size = 0
        
        for file in self.files:
            total_size += file.size

        for child_dir in self.child_directories:
            total_size += child_dir.size()

        return total_size

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return self.name

class Terminal:
    
    def __init__(self) -> None:
        self.history = []
        self.directories = []
        self.active_directory = None

    def execute_commands(self, lines: List[str]):
        while len(lines) > 0:
            command = lines.pop(0)
            split_string = command.split(" ")

            if len(split_string) == 3 and split_string[1] == "cd":
                self.change_directory(split_string[2])
            elif len(split_string) == 2 and split_string[1] == "ls":
                self.list_items(lines)
            else:
                pass


    def change_directory(self, location: str):
        if not self.active_directory:
            root_directory = Directory(location)
            self.active_directory = root_directory
            self.directories.append(root_directory)
            return

        if location == "..":
            self.active_directory = self.history.pop(0)
        else:
            self.history.insert(0, self.active_directory)
            child_directory = list(filter(lambda d: d.name == location, self.active_directory.child_directories))[0]
            self.active_directory = child_directory

    def list_items(self, lines: List[str]):
        while lines and not lines[0].startswith("$"):
            item = lines.pop(0)
            first, second = item.split(" ")
            directory = self.active_directory
            if first == "dir":
                new_directory = Directory(second)
                self.directories.append(new_directory)
                directory.child_directories.append(new_directory)
            else:
                file = File(second, int(first))
                directory.files.append(file)



terminal = Terminal()

with open("Day7.txt") as f:
    terminal.execute_commands([l.rstrip("\n") for l in f])

# PART 1 RESULT
max_size = 100000
directory_sizes = [(dir.name, dir.size()) for dir in terminal.directories]
print(sum(filter(lambda x: x < max_size, map(lambda d: d[1] ,directory_sizes))))

# PART 2 RESULT
max_space = 70000000

min_update_space = 30000000
used_space = max(directory_sizes, key=lambda dir: dir[1])[1]
needed_space = min_update_space - (max_space - used_space)

print(f"  USED SPACE: {used_space:10}")
print(f"NEEDED SPACE: {needed_space:10}")

candidate_directories = list(filter(lambda dir: dir[1] >= needed_space, directory_sizes))

print(min(candidate_directories, key=lambda dir: dir[1]))

