"""
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....

Here is some info on Unix file system paths:

    / is the root directory; the path should always start with it even if it isn't there in the given path;
    / is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;
        this also means that // stands for "change the current directory to the current directory"
    . is used to mark the current directory;
    .. is used to mark the parent directory; if the current directory is root already, .. does nothing.

Example

For path = "/home/a/./x/../b//c/", the output should be
simplifyPath(path) = "/home/a/b/c".

Here is how this path was simplified:
* /./ means "move to the current directory" and can be replaced with a single /;
* /x/../ means "move into directory x and then return back to the parent directory", so it can replaced with a single /;
* // means "move to the current directory" and can be replaced with a single /.
"""

def simplifyPath(path):
    dirs = path.split("/")
    print(dirs)
    
    dir2 = ['']
    for dir in dirs:
        
        # if ignore case
        if (dir == '') or (dir == '.'):
            continue
        
        # if move back case
        if (dir == '..'):
            if (len(dir2) > 0):
                dir2.pop()
            continue
            
        # if normal case
        dir2.append(dir)
        
    simple_path = '/'.join(dir2)
    if (len(simple_path) == 0 or simple_path[0] != '/'):
        simple_path = '/' + simple_path
    
    return simple_path


        
            
    
def main():
    path = "/home/a/./x/../b//c/"
    print(simplyPath(path))
    
main()