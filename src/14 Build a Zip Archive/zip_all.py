import zipfile
import pathlib
import os


def format_filter(fname: str, filters: list):
    for x in filters:
        if fname.lower()[-len(x):] == x:
            return True
    return False


def zip_all(src_dir: str | pathlib.Path,
            filters: list[str],
            outfile: str = None,
            zip_handle: zipfile.ZipFile = None,
            abs_root_path: pathlib.Path = None):
    src_dir = pathlib.Path(src_dir)
    abs_root_path = abs_root_path or src_dir.absolute().parent
    if not src_dir.exists():
        raise FileNotFoundError(f'Path {src_dir} does not exists')

    if not src_dir.is_dir():
        raise NotADirectoryError(f'Path {src_dir} is not a directory')

    try:
        if not zip_handle:
            if not outfile:
                raise ValueError(f'Parameter `outfile` is None')
            zip_handle = zipfile.ZipFile(outfile, 'w', zipfile.ZIP_DEFLATED)

        for fname in src_dir.iterdir():
            fname: pathlib.Path
            if outfile == fname.name:
                continue

            if fname.is_file():
                f_result = True
                if filters:
                    f_result = format_filter(fname.name, filters)
                if f_result:
                    rel_fname = os.path.relpath(fname, abs_root_path)
                    zip_handle.write(fname, arcname=rel_fname)
            elif fname.is_dir():
                zip_all(fname, filters, zip_handle=zip_handle, abs_root_path=abs_root_path)
            else:
                print(f'{fname} is not a directory and a file... [SKIPPED]')
    except:
        raise
    finally:
        if outfile:
            zip_handle.close()


zip_all(r'/workspaces/level-up-python-3210418/src/14 Build a Zip Archive/my_stuff', ['.jpg'], 'output1.zip')
zip_all('./my_stuff/', ['.png'], 'output2.zip')
