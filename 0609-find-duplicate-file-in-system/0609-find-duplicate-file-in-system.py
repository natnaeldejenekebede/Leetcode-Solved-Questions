class Solution:
    def findDuplicate(self, paths: List[str])  -> List[List[str]]:
        content_to_filepaths = {}
        duplicate_groups = []
        
        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                filename, content = file_info.split('(')
                if content in content_to_filepaths:
                    content_to_filepaths[content].append(directory + '/' + filename)
                else:
                    content_to_filepaths[content] = [directory + '/' + filename]
        
        for filepaths in content_to_filepaths.values():
            if len(filepaths) > 1:
                duplicate_groups.append(filepaths)
        
        return duplicate_groups
   
