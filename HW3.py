class SocialMedia:
    def __init__(self,name):
        self.app_name = name
        self.lst = []
    def getName(self):
        print (self.app_name)



class Instagram(SocialMedia):
    def __init__(self):
        super().__init__("Instagram")

    def publishNewPost(self,body):
        if len(body) < 2200:
            self.lst.append(body)
        else:
            print("length of the post should be under 2200")
        
    def getPosts(self):
        if len(self.lst) == 0:
            print("there is no posts")
            return -1
            
        print("instagram posts: ",self.lst)

class Twitter(SocialMedia):
    def __init__(self):
        super().__init__("Twitter")

    def createNewTweet(self,body):
        if len(body) < 280:
            self.lst.append(body)
        else:
            print("length of the tweet should be under 280")
    def getTweets(self):
        if len(self.lst) == 0:
            print("there is no tweets")
            return -1
        print("twitter tweets: ",self.lst)
            


body = input()


twitter = Twitter()
twitter.createNewTweet(body)

instagram = Instagram()
instagram.publishNewPost(body)

twitter.getName()
instagram.getName()


twitter.getTweets()
instagram.getPosts()
