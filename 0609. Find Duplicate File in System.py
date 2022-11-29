from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        file_contents = defaultdict(list)

        for entry in paths:
            content = entry.split(" ")
            directory = content[0]
            for i in range(1, len(content)):
                file_details = content[i]
                l = 0
                n = len(file_details)
                file_name = ""
                file_content = ""
                inside_file_content = False 
                while l <= n:
                    if file_details[l] == "(":
                        inside_file_content = True
                        l+=1
                    
                    if file_details[l] == ")":
                        break

                    if not inside_file_content:
                        file_name += file_details[l]

                    else :
                        file_content += file_details[l]
                    
                    l+=1
                file_contents[file_content].append(directory+"/"+file_name)
        
        ans = []
        for key, val in file_contents.items():
            if len(val) > 1:
                ans.append(val)
        
        return ans 





