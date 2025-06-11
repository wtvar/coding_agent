import os


def get_file_content(working_directory, file_path):
    #1
    #If the file_path is outside the working_directory, return a string with an error:
    #f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if abs_file_path.startswith(abs_working):
        pass
    else:
        #If the directory argument is outside the working_directory, return a string with an error:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    

    #2
    #If the file_path is not a file, again, return an error string:
    #f'Error: File not found or is not a regular file: "{file_path}"'
    if os.path.isfile(abs_file_path):
        pass
    else:
        return(f'Error: File not found or is not a regular file: "{file_path}"')
    #3
    #Read the file and return its contents as a string.
    MAX_CHARS = 10000
    #print(f"File exists: {os.path.exists(abs_file_path)}")
    #print(f"File readable: {os.access(abs_file_path, os.R_OK)}")
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            #print(type(file_content_string))
            #print(f"Length: {len(file_content_string)}")
            #print(f"Repr: {repr(file_content_string)}")
            if len(file_content_string) == MAX_CHARS:
                file_content_string += f"\n[...File '{file_path}' truncated at 10000 characters]"
            return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    #4
    #If the file is longer than 10000 characters, truncate it to 10000 characters and append this message to the end:
    #[...File "{file_path}" truncated at 10000 characters]


#tests

