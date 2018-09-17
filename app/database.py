from psycopg2 import connect
import numpy as np

def getClusters():
    #schema = 'trainning6000' ,dbUser = "cl-us-gzh",dbHost = "10.238.4.109",dbName = "cl-us-gzh",dbPass = "cl-us-gzh"
    try:
        conn = connect("dbname='cl-us-gzh' user='cl-us-gzh' host='10.238.4.109' password='cl-us-gzh'")
    except:
        print "I am unable to connect to the database"
    cur = conn.cursor()
    cur.execute("SET search_path TO trainning6000")
    cur.execute("SELECT user_email,cluster from clusters")
    clusters = []

    for reg in cur.fetchall():
        clusters.append(np.asarray(reg))
    cur.close()
    return clusters

def getClustersProfiles():
    #schema = 'trainning6000' ,dbUser = "cl-us-gzh",dbHost = "10.238.4.109",dbName = "cl-us-gzh",dbPass = "cl-us-gzh"
    try:
        conn = connect("dbname='cl-us-gzh' user='cl-us-gzh' host='10.238.4.109' password='cl-us-gzh'")
    except:
        print "I am unable to connect to the database"
    cur = conn.cursor()
    cur.execute("SET search_path TO trainning6000")
    cur.execute("SELECT cluster, tag, rec_idx from clusters_profiles")
    clusters_profiles = []

    for reg in cur.fetchall():
        clusters_profiles.append(np.asarray(reg))
    cur.close()
    return clusters_profiles

#getArticleUsersRecommendation("vinicius.rost@hotmail.com")
def getArticleUsersRecommendation(userEmail):
    #schema = 'trainning6000' ,dbUser = "cl-us-gzh",dbHost = "10.238.4.109",dbName = "cl-us-gzh",dbPass = "cl-us-gzh"
    try:
        conn = connect("dbname='cl-us-gzh' user='cl-us-gzh' host='10.238.4.109' password='cl-us-gzh'")
    except:
        print "I am unable to connect to the database"
    cur = conn.cursor()
    cur.execute("SET search_path TO trainning6000")
    sql = ("select cl.user_email, " +
          "       cl.cluster, " +
          "       sum(cp.rec_idx) " +
          "  from clusters cl inner join " +
          "       clusters_profiles cp on cl.cluster = cp.cluster " +
          " where cl.user_email = '{0}' " +
          " group by cl.user_email, cl.cluster").format(userEmail)
    cur.execute(sql)
    usersRecommendation = []

    for reg in cur.fetchall():
        usersRecommendation.append(np.asarray(reg))

    cur.close()
    return usersRecommendation