from utilities import process_json

class Story(object):
    def __init__(self):
        self.TalkData = []
        self.Character2dId = 0
        self.WindowDisplayName  = ""
        self.Body = ""

    def story(self, location1, location2, path: str):    
        data = process_json(location1, location2, path)
        self.TalkData = data["TalkData"]

      