import psycopg2

# host = "pg-dev-dev-101.a.aivencloud.com"
# port = "16506"
# dbname = "defaultdb"
# user = "avnadmin"
# password = "AVNS_WKCKGD4JC5s0lel9zKD"

# conn =  psycopg2.connect(("host={host} dbname={dbname} user={user} password={password} port={port}").format(host=host,dbname=dbname,user=user,password=password,port=port))

conn =  psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")

cur = conn.cursor()

# create table

cur.execute("""
            CREATE TABLE IF NOT EXISTS users_using_copy(
                id serial primary key
                ,email text
                ,name text
                ,phone text
                ,postal_code text
            )
            """)

with open("C:/Users/User/OneDrive/Documents/File Kerjaan/melamar kerjaan/arry/Project automation/PROJECT DE16/Project 3/source/users_w_postal_code.csv","r") as f :
    next(f)
    cur.copy_from(f, "users_using_copy", sep=",", columns=("email","name","phone","postal_code"))

conn.commit()