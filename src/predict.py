import pickle

'''
subscriberCount
channelVideoCount
channelViewCount
PrevCommentCount
PrevDislikeCount
PrevLikeCount
PrevViewCount
Title-clickbait score
nsfw score 
Motivation
Transform
Published Year 
Channel Age
'''
class Predictor(object):
    def __init__(self, model_path):
        self.model  = pickle.load(open(model_path, "rb"))

    def predict(self, click_bait_score, nsfw_score, youtube_id = ""):
        subscriberCount = 0




predictor = Predictor("models/view_count/xgb001.pickle.dat")