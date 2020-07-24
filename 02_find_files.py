import os

def find_files(suffix, path):
    """
    Finds all files beneath path with file name suffix.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    ls = os.listdir(path)
    files = []

    for item in ls:
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            files += find_files(suffix, item_path)

        if os.path.isfile(item_path) and item.endswith(suffix):
            files.append(item_path)

    return files

test_path = '/home/b/Documents/Udacity/Python/P1/testdir'
suffix = 'c'

# traverses subsub directory
actual = find_files( suffix, os.path.join(test_path, 'subdir3') ) 
expect = ['/home/b/Documents/Udacity/Python/P1/testdir/subdir3/subsubdir1/b.c']
assert(actual == expect)

# finds all four recursive matches
actual = len( find_files(suffix, test_path) )
expect = 4
assert(actual == expect)

# finds another four recursive matches
actual = len( find_files('h', test_path) )
expect = 4
assert(actual == expect)

for file_path in find_files('c', test_path):
    print(file_path)
