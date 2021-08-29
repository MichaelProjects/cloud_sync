import os


class FileManagement:

    def __init__(self):
        self.storage_path = os.environ["storage_path"]


    # basic file operations
    
    def insert_file(self):
        pass

    def delete_file(self):
        pass
    
    def insert_dir(self):
        pass

    def delete_dir(self):
        pass

    # advanced file operations

    def get_all_files_dirs(self):
        dir = []
        files = []
        for (dir_path, dir_name, filename) in os.walk(self.storage_path):
            dir.append(dir_path)
            files.append(filename)
        return {"dirs": dir, "files": files}
        
