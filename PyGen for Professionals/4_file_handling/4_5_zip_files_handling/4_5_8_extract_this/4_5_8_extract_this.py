'''
TODO:
    Implement the extract_this() function that takes one or more arguments
    in the following order:
        zip_name — the name of the zip archive, for example, data.zip
        *args — a variable number of positional arguments,
                each of which is the name of some file

    The function should extract the files *args from the zip_name archive
    to the program folder.

    If no file names are passed to the function for extraction, the
    function should extract all files from the archive.

NOTE:

    For example, the following call to the
        extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
    function should extract the earth.jpg and exam.txt files from the
    workbook.zip archive to the program folder.

    The call to the extract_this('workbook.zip') function should extract
    all files from the workbook.zip archive to the program folder.
'''
from zipfile import ZipFile


def _extract_all_files_from_zip(
    zip_name: str, destination_path: str = ''
) -> None:
    """
    Extracts all files from the specified zip archive to the given
    destination path.

    Args:
        zip_name (str): The name of the zip archive.
        destination_path (str): The path to extract files to. Defaults to
                                 the current directory.

    Returns:
        None
    """
    with ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(destination_path)


def _extract_file_from_zip(
    zip_name: str, file_name: str, destination_path: str = ''
) -> None:
    """
    Extracts a single file from the specified zip archive to the
    given destination path.

    Args:
        zip_name (str): The name of the zip archive.
        file_name (str): The name of the file to extract.
        destination_path (str): The path to extract the file to. Defaults
                                 to the current directory.

    Returns:
        None
    """
    with ZipFile(zip_name, 'r') as zipf:
        zipf.extract(file_name, destination_path)


def extract_this(
    zip_name: str, *args: str, destination_path: str = ''
) -> None:
    """
    Extracts specified files from the zip archive to the given
    destination path. If no file names are provided, all files will
    be extracted.

    Args:
        zip_name (str): The name of the zip archive.
        args (str): The names of the files to extract. If no names are
                    provided, all files will be extracted.
        destination_path (str): The path to extract files to. Defaults to
                                 the current directory.

    Returns:
        None
    """
    if args:
        for filename in args:
            _extract_file_from_zip(zip_name, filename, destination_path)
    else:
        _extract_all_files_from_zip(zip_name, destination_path)
