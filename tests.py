

# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content




if __name__ == "__main__":

    """
    get files tests
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "pkg"))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
    """
    #get_content tests
    print("test1")
    print(get_file_content("calculator", "lorem.txt"))
    print("test2")
    print(get_file_content("calculator", "main.py"))
    print("test3")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("test4")
    print(get_file_content("calculator", "/bin/cat")) #(this should return an error string)



