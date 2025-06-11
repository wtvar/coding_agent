import os



def get_files_info(working_directory, directory=None):
    #If the directory argument is not a directory, again, return an error string:
    full_sub = os.path.join(working_directory,directory)
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))
    #print(f'directory: {directory}')
    #print(f'working_directory: {working_directory}')
    #print(f'full: {full_sub}')
    #print(f'abs_working: {abs_working}')
    #print(f'abs_target: {abs_target}')
    

    if abs_target.startswith(abs_working):
        pass
    else:
        #If the directory argument is outside the working_directory, return a string with an error:
        #print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if os.path.isdir(abs_target):    #os.path.isdir(): Check if a path is a directory
        pass
    else:
        #print(f'Error: "{directory}" is not a directory')
        return(f'Error: "{directory}" is not a directory')
    
    list_of_lines = []
    for file in os.listdir(abs_target):
        #print(file)
        abs_file = os.path.join(abs_target,file)
        file_name = file
        file_size = os.path.getsize(abs_file)
        is_dir = os.path.isdir(abs_file)
        return_string = f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}'
        #print(f'return: {return_string}')
        list_of_lines.append(return_string)
        #print(return_string)
        #print(f'total: {total_string}')

    return '\n'.join(list_of_lines)


"""
root = "."
get_files_info(root, directory="functions")

print(get_files_info("calculator", "../"))
print(get_files_info("calculator", "/bin"))
"""
"""
build and return string:

- README.md: file_size=1032 bytes, is_dir=False
- src: file_size=128 bytes, is_dir=True
- package.json: file_size=1234 bytes, is_dir=False

useful funcs:

    os.path.abspath(): Get an absolute path from a relative path
    os.path.join(): Join two paths together safely (handles slashes)
    .startswith(): Check if a string starts with a substring
    os.path.isdir(): Check if a path is a directory
    os.listdir(): List the contents of a directory
    os.path.getsize(): Get the size of a file
    os.path.isfile(): Check if a path is a file
    .join(): Join a list of strings together with a separator

"""