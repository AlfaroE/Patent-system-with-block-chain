import hashlib

def get_hash(file,block_size):
    file_hash = hashlib.sha512()
    with open(file,'rb') as f:
        fb = f.read(block_size)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(block_size)
    
    return file_hash.hexdigest()