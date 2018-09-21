import database as db
import numpy

class Recommender:
    def __init__(self):
        self.database = db.DataBase()
        self.clusters = numpy.array([])
        self.clusters = numpy.array(self.database.getClusters())
        self.clustersProfiles = numpy.array([])
        self.clustersProfiles = numpy.array(self.database.getClustersProfiles())

    def update(self):
        self.clusters = numpy.array(self.database.getClusters())
        self.clustersProfiles = numpy.array(self.database.getClustersProfiles())

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    def getArticleUsersRecommendations(self, articleTags, users):
        articleUsersRecommendations = []
        for user in users:
            cluster = self.clusters[self.clusters[:, 0] == user, 1]
            recIdx = 0
            for tag in articleTags:
                recIdx += float(self.clustersProfiles[self.clustersProfiles[:, 1] == tag,][self.clustersProfiles[self.clustersProfiles[:, 1] == tag, 0] == cluster, 2])
            articleUsersRecommendations.append([user,recIdx])
        return articleUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each article based on the user's cluster profile
    def getArticlesUserRecommendations(self, articles, user):
        articlesUserRecommendations = []

        cluster = self.clusters[self.clusters[:, 0] == user, 1]

        for article in articles:
            recIdx = 0
            for tag in article["tags"]:
                recIdx += float(self.clustersProfiles[self.clustersProfiles[:, 1] == tag,][self.clustersProfiles[self.clustersProfiles[:, 1] == tag, 0] == cluster, 2])
            articlesUserRecommendations.append([article["article"], recIdx])

        return articlesUserRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    def getArticlesUsersRecommendations(self, articlesTags, users):
        articlesUsersRecommendations = []

        return articlesUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles that match the user's clusterProfile and the article's tags
    def getArticleUserArticlesRecommendations(self, articleTags, user, articlesTags):
        articlesUserRecommendations = []
        return articlesUserRecommendations