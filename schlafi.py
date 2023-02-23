import discord, pickle, json, datetime

def cut(toCut,inputString):
    if len(inputString)>=len(toCut):
        if inputString[:len(toCut)]==toCut:
            return inputString[len(toCut):]
    return inputString

def defaultConfig():
    return {
        "token": "token",
        "prefix": "!",
        "optional": {
            "quote": "No quote set - schlafi, 2023",
            "time": [0,0]
        }
    }

def readFromConfig(key):
    config=defaultConfig()
    with open("config.json","r") as f:
        tmpconfig=json.load(f)
        for key in tmpconfig:
            config[key]=tmpconfig[key]
    if key in config:
        return config[key]
    else:
        if key in config["optional"]:
            return config["optional"][key]
    
def writeToConfig(key,value):
    config=defaultConfig()
    with open("config.json","r") as f:
        tmpconfig=json.load(f)
        for key in tmpconfig:
            config[key]=tmpconfig[key]
    if key in config["optional"]:
        config["optional"][key]=value
    else:
        config[key]=value
    with open("config.json","w") as f:
        json.dump(config,f)

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

class cQuote(command):
    def __init__(self):
        super().__init__("quote","Sets the quote.")
        quote=readFromConfig("quote")
    def execute(self,message):
        c=message.contents
        quote=cut(prefix+self.name,c).strip()
        writeToConfig("quote",quote)
    
        

class cSetTime(command):
    def __init__(self):
        super().__init__("settime","Sets the time.")
        self.time=[0,0]
    def execute(self,message):
        c=message.contents
commands={
   "help": cHelp()
}