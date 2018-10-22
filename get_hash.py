import hashlib
import argparse
import pathlib
import logging
# logging
logging.basicConfig(level=logging.DEBUG) ###DEBUG
logger = logging.getLogger(__name__)


def filehash(file):
    logger.debug("filepath:%s", file)
    hash = hashlib.sha1()
    try:
        with open(file, 'rb') as f:
            while True:
                chunk = f.read(2048 * hash.block_size)
                if len(chunk) == 0:
                    break
                hash.update(chunk)
        digest = hash.hexdigest()
        return digest
    except PermissionError:
        logger.error("PermissionErro:%s", file)
        return 0


def get_path(path):
    files =[]
    if path.is_file():
        logger.debug("path:%s", str(path))
        filename = path.resolve()
        logger.debug("filename:%s", filename)
        files.append(filename)
    elif path.is_dir():
        for p in path.iterdir():
            files.extend(get_path(p))
    logger.debug("files:%s", files)
    return files

def main():
    current = pathlib.Path('c:\doc')
    ans = get_path(current)
    print(ans)
    for filename in ans:
        p = pathlib.Path(filename)
        
        logger.debug("filename:%s, time:%s, hash:%s", filename, p.stat().st_mtime, filehash(filename))
        print(filename,":", "(", p.stat().st_mtime, ",", filehash(filename), ")")
    

def _main():
    try:
        parser = argparse.ArgumentParser(description='hashApp')
        parser.add_argument('filepath', help='Input file path')
        args = parser.parse_args()

        filepath = args.filepath
        digest = filehash(filepath)

        print("\"{0}\" : {1}".format(filepath, digest))
    except ValueError:
        print("error!")
    except SystemExit:
        print("parser exit!")



if __name__ == '__main__':
    main()


        
