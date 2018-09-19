from recommender import *
import json

if __name__ == "__main__":
    recommender = Recommender()
    tags = ['futebol','gremio','brasileirao']
    users =['biancamn@gmail.com', 'bobkingg@gmail.com','alessandra.damaia@hotmail.com']
    print(recommender.getArticleUsersRecommendations(articleTags=tags, users=users))
    print(json.dumps(recommender.getArticleUsersRecommendations(articleTags=tags, users=users)))
    #print(json.dumps(numpy.ndarray.tolist(recommender.clusters)))

