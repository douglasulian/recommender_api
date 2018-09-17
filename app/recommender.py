import database as db

class Recommender:
    def __init__(self):
        self.clusters = db.getClusters()
        self.clustersProfiles = db.getClustersProfiles()

    def update(self):
        self.clusters = db.getClusters()
        self.clustersProfiles = db.getClustersProfiles()

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    def getArticleUsersRecommendations(self, articleTags, users):
        articleUsersRecommendations = []
        return articleUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each article based on the user's cluster profile
    def getArticlesUserRecommendations(self, articlesTags, user):
        articlesUserRecommendations = []
        return articlesUserRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    def getArticlesUsersRecommendations(self, articlesTags, users):
        articlesUsersRecommendations = []
        return articlesUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles that match the user's clusterProfile and the article's tags
    def getArticleUserArticlesRecommendations(self, articleTags, user, articlesTags):
        articlesUserRecommendations = []
        return articlesUserRecommendations