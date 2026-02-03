class Instagram:
    def __init__(self,title,description):
        self.title=title
        self.description=description
        self.like=0
    def display_title(self):
        print("the title of the reel is",self.title)
    def display_description(self):
        print("the decription of the reel is",self.description)
    def display_like(self):
        print("the number of likes is",self.like)
    def liked(self):
        self.like +=1
    def disliked(self):
        if self.like >0:
            self.like -=1


reel=Instagram("singing","singing with bro")
reel.display_title()
reel.display_description()
reel.liked()
reel.display_like()
reel.disliked()
reel.display_like()

reel2=Instagram("dancing","dancing with bro")
reel.disliked()
reel.display_like()


print(id(reel))
print(id(reel2))