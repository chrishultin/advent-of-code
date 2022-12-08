from __future__ import annotations
from dataclasses import dataclass
import typing

INPUT_FILE = 'input.txt'

@dataclass
class File:
    size: int

@dataclass
class Directory:
    directories: typing.Dict[str, Directory]
    files: typing.Dict[str, File]

    def get_size(self):
        size = 0
        for i in self.directories.values():
            size += i.get_size()
        for i in self.files.values():
            size += i.size

        return size

    def get_big_dir(self, min_size: int):
        big_directories = []
        for dir in self.directories.values():
            big_directories.extend(dir.get_big_dir(min_size))

        size = self.get_size()
        if size < min_size:
            big_directories.append(size)

        return big_directories

root_dir = Directory(directories={}, files={})

current_directory = root_dir
directory = Directory(directories={'/': root_dir}, files={})

with open(INPUT_FILE, 'r') as input_file:
    current_path = ['/']
    #skip first line
    command_line = input_file.readline()
    while True:
        command_line = input_file.readline().strip()
        if not command_line:
            break

        command_params = command_line.split(' ')

        if command_params[0] == '$':
            if command_params[1] == 'ls':
                pass
            elif command_params[1] == 'cd' and command_params[2] == '..':
                # Remove current directory from path; Reset to Root Dir
                current_path.pop()
                current_directory = directory
                for i in current_path:
                    # Progressively navigate through the path to the expected directory
                    current_directory = current_directory.directories[i]
            else:
                current_path.append(f'{command_params[2]}')
                current_directory = current_directory.directories.get(command_params[2])

        else:
            if command_params[0] == 'dir':
                current_directory.directories[command_params[1]] = Directory(directories={}, files={})
            else:
                size = command_params[0]
                name = command_params[1]
                print(f'adding {command_params[1]} to current dir')
                current_directory.files[name] = File(size=int(size))

    # print(directory)
    # print(directory.get_size())
    print(directory.get_big_dir(100000))
    total_bigdir_size = 0
    for i in directory.get_big_dir(100000):
        total_bigdir_size += i

    print(total_bigdir_size)