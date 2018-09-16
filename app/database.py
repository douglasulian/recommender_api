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

    return clusters