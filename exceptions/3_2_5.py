# file_to_open = data_folder / "raw_data.txt"
# import os
# wd = os.getcwd()

def read_file(file_name):
    try:
        f = open(file_name, 'r')
        try:
            print("__CONTENT_START__")
            output = f.read()
        finally:
            f.close()
            print("__FILED_CLOSED__")
    except FileNotFoundError:
        print("__CONTENT_START__")
        print("__NO_SUCH_FILE__")
    else:
        print("__PRINTING_FILE_CONTENT_ELSE__")
        print(output)
        # f.close()
    finally:
        print("__CONTENT_END__")
    



read_file('file.txt')


# read_file("/Users/erezsh/work/campus_il/exceptions/ile.txt")
# with open(wd + '/file.txt', 'r') as f:
# with open('file.txt', 'r') as f:
#     output = f.read()

# print(output)




# print(output)
# import os
# os.getcwd() 