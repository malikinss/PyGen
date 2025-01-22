'''
TODO:
    A dangerous virus has penetrated the file system of the computer on which
    our ❤️ Stepik platform is deployed and broken the file access rights
    control.

    They say that the virus was written by one of the students of the Python
    for Beginners course.

    For each file, it is known what actions can be used to access it:
        - Write (write, access to write to the file);
        - Read (read, access to read from the file);
        - Run X (execute, run the file for execution).

    Write a program to restore file access rights control.

    For each request, your program should return OK if the operation
    is allowed, and Access denied if the operation is not allowed.
'''

actions_dict = {'execute': 'X', 'write': 'W', 'read': 'R'}


def get_new_filesystem(number_files: int) -> dict:
    """
    Creates a dictionary representing the filesystem with access rights for
    each file.

    Args:
        number_files (int): Number of files to process.

    Returns:
        dict: Filesystem dictionary where keys are filenames and values are
              lists of access rights.
    """
    filesystem = {}

    for _ in range(number_files):
        data = input().split()
        filename, access_rights = data[0], data[1:]
        filesystem[filename] = access_rights

    return filesystem


def try_to_work_with_files(
    number_requests: int, actions_dict: dict, filesystem: dict
) -> None:
    """
    Processes user requests to access files and outputs whether the operation
    is allowed or denied.

    Args:
        number_requests (int): Number of file access requests.
        actions_dict (dict): Mapping of action names to their corresponding
                             codes.
        filesystem (dict): Dictionary of files and their respective access
                           rights.
    """
    for _ in range(number_requests):
        action, filename = input().split()
        action_code = actions_dict.get(action)

        if filename in filesystem and action_code in filesystem[filename]:
            print('OK')
        else:
            print('Access denied')


# Input handling and program execution
new_filesystem = get_new_filesystem(int(input()))
try_to_work_with_files(int(input()), actions_dict, new_filesystem)
