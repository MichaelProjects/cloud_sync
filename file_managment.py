import os


class FileManagement:

    def __init__(self):
        self.storage_path = os.environ["storage_path"]


    # basic file operations
    
    def insert_file(self, name, path, data):
        

    def delete_file(self):
        pass
    
    def insert_dir(self):
        pass

    def delete_dir(self):
        pass

    # advanced file operations

    def get_all_files_dirs(self):
        result = []
        for (dir_path, dir_name, filename) in os.walk(self.storage_path):
            data = {"dir": dir_path.split(self.storage_path)[1], "files": filename, "subdir": dir_name}
            result.append(data)
        return {"cloud_sync":result}
        
