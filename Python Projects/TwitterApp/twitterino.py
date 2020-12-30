#Import the good stuff:
import json
#import re
from twitter import Twitter, OAuth 
import random 
import matplotlib.pyplot as plt


class twitterwinnerino():
    def __init__(self):
        ACCESS_TOKEN = '987308304815869954-VipB3jthaUyT0hcLtPq9S3RQmpoDyR4'
        ACCESS_SECRET = 'sZDDz0LGO27YRe6FARDDIGl69QyeMggIllSfVu1ibQ2cW'
        CONSUMER_KEY = '2Npkq80Axd2lUr4Ui1nrhJAbw'
        CONSUMER_SECRET = 'S57PgJCpLAVOU7AtiztZl7altAt5LONCxJycDslFlIVo1t03Jn'
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET,
                      CONSUMER_KEY, CONSUMER_SECRET)
        self.t = Twitter(auth=oauth)

        self.hashtag_1 = ""
        self.hashtag_2 = ""
        self.counter = 0
        self.a = []
        self.b = []
        self.user_list_1 = []
        self.user_list_2 = []
        self.winner_list = []
        self.numberlist = 0
        self.new_winnerlist = []
        self.graph_dic = {}

    def counterino(self, numberino):
        self.counter = numberino
        
    def refreshGUI(self):
        self.numberlist = 0
        self.user_list_1 = []
        self.user_list_2 = []
        self.winner_list = []
        self.new_winnerlist = []
        self.a = []
        self.b = []

    def hashtagerino_1(self, input_hash_1):
        self.hashtag_1 = input_hash_1
        print("1. #" + self.hashtag_1)
        # Filling in the tweet information in list a:
        self.query_a = self.t.search.tweets(q=self.hashtag_1)

        for s in self.query_a['statuses']:
            self.a.append(json.loads(json.dumps(s)))

        # Put the Id of every tweet in the user_list_1
        for i in range(len(self.a)):
            self.item = self.a[i]["id"]
            self.user_list_1.append(self.item)

    def hashtagerino_2(self, input_hash_2):
        self.hashtag_2 = input_hash_2
        print("2. #" + self.hashtag_2)
        # Filling in the tweet information in list b:
        self.query_b = self.t.search.tweets(q=self.hashtag_2)

        for s in self.query_b['statuses']:
            self.b.append(json.loads(json.dumps(s)))

        # Same thing for user_list_2:
        for i in range(len(self.b)):
            self.item = self.b[i]["id"]
            self.user_list_2.append(self.item)

    def winnerino(self):
        # Compare user_lists and give location of same user id:
        self.winner_id = set(self.user_list_1) & set(self.user_list_2)
        self.winner_id_list = list(self.winner_id)
        self.winner_list = []
        # Search user id in original tweet list:
        if len(self.winner_id_list) > 0:
            print(len(self.winner_id_list))
            for i in range(len(self.a)):
                self.check = self.a[i]["id"]
                for j in range(len(self.winner_id_list)):
                    self.check_2 = self.winner_id_list[j]
                    if self.check_2 == self.check:
                        if self.a[i]["user"]["location"] == "":
                            self.z = self.a[i]["user"]["screen_name"] + " from: unknown location"
                        else:
                            self.z = self.a[i]["user"]["screen_name"] + " from: " + self.a[i]["user"]["location"]
                        self.winner_list.append(self.z)
            print(len(self.winner_list))
            print(len(self.user_list_1))
            print(len(self.user_list_2))

            if len(self.winner_list) >= self.counter:
                print(self.counter)
                self.winner = random.sample(population=self.winner_list, k=self.counter)
                self.numberlist = []
                self.new_winnerlist = []
                for i in range(len(self.winner)):
                    self.numberlist.append(str(i+1))
                for j in range(len(self.winner)):
                    self.new_winnerlist.append(self.numberlist[j] + ": @" + self.winner[j])                   
                return(self.new_winnerlist)

            elif len(self.winner_list) < self.counter:
                self.winner = random.sample(population=self.winner_list, k=len(self.winner_list))
                self.numberlist = []
                self.new_winnerlist = []
                for i in range(len(self.winner)):
                    self.numberlist.append(str(i+1))
                for j in range(len(self.winner)):
                    self.new_winnerlist.append(self.numberlist[j] + ": @" + self.winner[j])
                self.new_winnerlist = ["Winners found < Count"] + self.new_winnerlist                   
                return(self.new_winnerlist)

        else:
            self.winner = str("The list is empty, use another pair of hashtags")
            return str(self.winner)

    def appenddict(self):
        print("len of #1: " + str(len(self.user_list_1)))
        print("len of #2: " + str(len(self.user_list_2)))
        self.graph_dic[self.hashtag_1] = len(self.user_list_1)
        self.graph_dic[self.hashtag_2] = len(self.user_list_2)
        if len(self.winner_list) > 0:
            self.graph_dic[self.hashtag_1 + ", " + self.hashtag_2] = len(self.winner_list)
        elif len(self.winner_list) == 0:
            self.graph_dic[self.hashtag_1 + ", " + self.hashtag_2] = 0
        print(self.graph_dic)

        x = list(self.graph_dic.keys())
        y = list(self.graph_dic.values())
        x_pos = [i for i, _ in enumerate(x)]

        plt.bar(x_pos, y, color='steelblue')
        plt.xlabel("Hashtags")
        plt.ylabel("Count")
        plt.title("History of searched hashtags")

        plt.xticks(x_pos, x)

        plt.show()
