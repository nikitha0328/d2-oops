class Instagram:
    def __init__(self,title,description,creator_name,location):
        self.title=title
        self.description=description
        self.like=0
        self.creator_name=creator_name
        self.location=location
        self.comments=[]

    def display_title(self):
        print("the title of the reel is ",self.title)
    def display_description(self):
        print("the description of the reel is",self.description)
    def display_like(self):
        print("the likes is ",self.like)
    def liked(self):
        self.like +=1
    def disliked(self):
        if self.like >0:
            self.like -=1
    def display_creator_name(self):
        print("the name of creator is",self.creator_name)
    def display_location(self):
        print("the location is",self.location)
    def display_comment(self):
        print("the comments are")
        if len(self.comments)==0:
            print("this is empty comment")
        else:
            for comment in self.comments:
                print("-",comment)
    def add_comments(self,comment):
        self.comments.append(comment)
    def delete_last_comments(self):
        temp_comment=self.comments.pop()
        print("the last comment is deleted",temp_comment)

reel1=Instagram("dancing","dancing with frd","john","china")
reel1.add_comments("comment1")
reel1.display_comment()
reel1.delete_last_comments()
reel1.display_comment()