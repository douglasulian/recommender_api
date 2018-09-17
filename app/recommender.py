#import database as db
import numpy


class Recommender:
    def __init__(self):
        self.clusters = numpy.array([])
        self.clusters = numpy.array(getClusters())
        self.clustersProfiles = numpy.array([])
        self.clustersProfiles = numpy.array(getClustersProfiles())


    def update(self):
        self.clusters = numpy.array(getClusters())
        self.clustersProfiles = numpy.array(getClustersProfiles())

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    #teste.getArticleUsersRecommendations(['futebol','gremio','brasileirao'], ['biancamn@gmail.com', 'bobkingg@gmail.com','alessandra.damaia@hotmail.com'])
    def getArticleUsersRecommendations(self, articleTags, users):
        articleUsersRecommendations = []
        for user in users:
            cluster = self.clusters[self.clusters[:, 0] == user, 1]
            recIdx = 0
            for tag in articleTags:
                recIdx += self.clustersProfiles[self.clustersProfiles[:, 1] == tag,][self.clustersProfiles[self.clustersProfiles[:, 1] == tag, 0] == cluster, 2]
            articleUsersRecommendations.append([user,recIdx])
        return articleUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each article based on the user's cluster profile
    # teste.getArticlesUserRecommendations([['noticia futebol',['futebol','gremio','brasileirao']],['noticia emprego',['contratacao']]], ['biancamn@gmail.com'])
    def getArticlesUserRecommendations(self, articlesTags, user):
        articlesUserRecommendations = []

        cluster = self.clusters[self.clusters[:, 0] == user, 1]

        for articleTags in articlesTags:
            recIdx = 0
            for tag in articleTags[1]:
                recIdx += self.clustersProfiles[self.clustersProfiles[:, 1] == tag,][
                    self.clustersProfiles[self.clustersProfiles[:, 1] == tag, 0] == cluster, 2]
            articlesUserRecommendations.append([articleTags[0], recIdx])

        return articlesUserRecommendations

    # sums the corresponding rec_idx from clustersProfiles for each user based on the user's cluster
    def getArticlesUsersRecommendations(self, articlesTags, users):
        articlesUsersRecommendations = []
        return articlesUsersRecommendations

    # sums the corresponding rec_idx from clustersProfiles that match the user's clusterProfile and the article's tags
    def getArticleUserArticlesRecommendations(self, articleTags, user, articlesTags):
        articlesUserRecommendations = []
        return articlesUserRecommendations