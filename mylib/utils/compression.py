import zipfile as _zipfile
import gzip as _gzip
import os as _os

def zip_files(output_path, file_paths):
    with _zipfile.ZipFile(output_path, "w") as zipf:
        for file_path in file_paths:
            if _os.path.isfile(file_path):
                zipf.write(file_path, arcname=_os.path.basename(file_path))

def unzip_file(zip_path, output_dir):
    if not _os.path.exists(output_dir):
        _os.makedirs(output_dir)

    with _zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(output_dir)

def gzip_file(input_path, output_path):

    if not _os.path.isfile(input_path):
        raise FileNotFoundError(f"No such file: {input_path}")

    with open(input_path, "rb") as f_in:
        with _gzip.open(output_path, "wb") as f_out:
            f_out.writelines(f_in)

def gunzip_file(input_path, output_path):
    if not _os.path.isfile(input_path):
        raise FileNotFoundError(f"No such file: {input_path}")
    
    with _gzip.open(input_path, "rb") as f_in:
        with open(output_path, "wb") as f_out:
            f_out.writelines(f_in)