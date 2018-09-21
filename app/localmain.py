from recommender import *
import json

if __name__ == "__main__":
    body = ('{' +
             '"users": ["biancamn@gmail.com",' +
                       '"bobkingg@gmail.com",' +
                       '"alessandra.damaia@hotmail.com"' +
                      '],' +
             '"tags": ["futebol",'
                      '"gremio",' +
                      '"brasileirao"' +
                     ']' +
             '}')

    bodyJson = json.loads(body)
    tags = bodyJson["tags"]
    users = bodyJson["users"]
    #tags = ['futebol','gremio','brasileirao']
    #users =['biancamn@gmail.com', 'bobkingg@gmail.com','alessandra.damaia@hotmail.com']
    recommender = Recommender()

    print(json.dumps(recommender.getArticleUsersRecommendations(articleTags=tags, users=users)))

    body = ('{' +
            '  "articles": [' +
            '    {' +
            '      "article": "1",' +
            '      "tags": [' +
            '        "futebol"' +
            '      ]' +
            '    },' +
            '    {' +
            '      "article": "2",' +
            '      "tags": [' +
            '        "futebol",' +
            '        "gremio"' +
            '      ]' +
            '    },' +
            '    {' +
            '      "article": "3",' +
            '      "tags": [' +
            '        "futebol",' +
            '        "gremio",' +
            '        "brasileirao"' +
            '      ]' +
            '    }' +
            '  ],' +
            '  "user": "biancamn@gmail.com"' +
            '}')
    bodyJson = json.loads(body)
    articles = bodyJson["articles"]
    user = bodyJson["user"]

    print(json.dumps(recommender.getArticlesUserRecommendations(articles=articles, user=user)))
    #print(json.dumps(numpy.ndarray.tolist(recommender.clusters)))

    body = ('{' +
            '  "articles": [' +
            '    {' +
            '      "article": "1",' +
            '      "tags": [' +
            '        "futebol"' +
            '      ]' +
            '    },' +
            '    {' +
            '      "article": "2",' +
            '      "tags": [' +
            '        "futebol",' +
            '        "gremio"' +
            '      ]' +
            '    },' +
            '    {' +
            '      "article": "3",' +
            '      "tags": [' +
            '        "futebol",' +
            '        "gremio",' +
            '        "brasileirao"' +
            '      ]' +
            '    }' +
            '  ],' +
            '  "users": [' +
            '    "biancamn@gmail.com",' +
            '    "bobkingg@gmail.com",' +
            '    "alessandra.damaia@hotmail.com"' +
            '  ]' +
            '}')