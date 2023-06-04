from utilities import process_json

class UnitStory(object):
    def __init__(self):
        self.TalkData = []
        self.Character2dId = 0
        self.WindowDisplayName  = ""
        self.Body = ""

    def unit_story(self, path: str):    
        data = process_json(path)
        self.TalkData = data["TalkData"]

      