import discord, pickle, json, datetime

class note:
    def __init__(self, authorID, content, due):
        self.authorID = authorID
        self.content = content
        self.due = due
        self.startDate = datetime.datetime.now()

class command:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def getInfo(self):
        return self.name + " - " + self.description
    def execute(self, message):
        pass
    
class cHelp(command):
    def __init__(self):
        super().__init__("help", "Shows this help")
    def execute(self, message):
        global commands
        out=""
        for command in commands:
            out += commands[command].getInfo() + "\n"
        message.channel.send(out)
        
commands={
   "help": cHelp()
}