class Trei:
    def __init__(self,isDirectory):
        self.child = {}
        self.content = ""
        self.isDirectory = isDirectory
    
    def insert(self,path,content):
        current = self
        pathList = [p for p in path.split("/") if p]
        for p in pathList:
            if p not in current.child:
                current.child[p] = Trei(True)
            current = current.child[p]
        if content:
            current.isDirectory = False
            current.content += content

    def getNode(self,path):
        cur = self
        pathList = [p for p in path.split("/") if p]
        for p in pathList:
            cur = cur.child[p]
        return cur
    
    def ls(self,path):
        current = self.getNode(path)
        if current.isDirectory:
            return sorted(list(current.child.keys()))
        return [path.split("/")[-1]]
    
    def getContent(self,path):
        return self.getNode(path).content

class FileSystem:

    def __init__(self):
        self.trei = Trei(True)
        

    def ls(self, path: str) -> List[str]:
        return self.trei.ls(path)
        

    def mkdir(self, path: str) -> None:
        self.trei.insert(path,None)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.trei.insert(filePath,content)
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.trei.getContent(filePath)
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)


    #                 /
    #             a
    #         /
    #         b   
    #     /           /
    #     c          e
    # /              /
    # d = Hello.    f = Thanks

    # for ls I go through the tree once I reach destination I check if content not empty
    # . If a file then return file name + child names. 
    # then sort the list and return

    # mkdir is just add required children to the trei

    # addContentToFile = mkdir + add content for last child

    # readContentFromFile = just get data from child node


