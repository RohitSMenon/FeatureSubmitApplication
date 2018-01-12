import json
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
from database import insert
import collections
def insert(data):

    print data
    # get data from json
    title = data["title"]
    description = data["description"]
    client = data["client"]
    clientPriority = data["clientPriority"]
    targetDate = data["targetDate"]
    product = data["productArea"]

    #create temporary db
    engine = create_engine('sqlite:///featureRequest.db',echo=True)
    metadata = MetaData(bind=engine)
    requests = Table('requests', metadata,
    Column('request_id', Integer, primary_key=True),
    Column('title', String(40)),
    Column('description', String(200)),
    Column('client', String(30)),
    Column('clientPriority', Integer),
    Column('targetDate', String(10)),
    Column('productArea', String(50)),
    )
    requests.create(checkfirst=True)

    #insert data to temporary table
    i = requests.insert()
    i.execute(title=title,description=description,client=client,clientPriority=clientPriority,targetDate=targetDate,productArea=product)
    s = requests.select()
    rs = s.execute()
    row = rs.fetchone()

    print 'Id:', row[0]
    print 'title:', row['title']
    print 'targetDate:', row['targetDate']
    print 'clientPriority:', row.clientPriority
    for row in rs:
        print row.title, '-', row.description, '!!!'
    return "Saved Successfully. Request ID - "+ str(row[0])
def getData():
    engine = create_engine('sqlite:///featureRequest.db',echo=True)
    rs= engine.execute('SELECT * FROM "requests"')
    objects_list = []
    for row in rs:
        d = collections.OrderedDict()
        d['request_id'] = row.request_id
        d['title'] = row.title
        d['description'] = row.description
        d['client'] = row.client
        d['clientPriority'] = row.clientPriority
        d['targetDate'] = row.targetDate
        d['productArea'] = row.productArea
        objects_list.append(d)
    j = json.dumps(objects_list)
    print'00000000000000000000000'
    print j
    print'00000000000000000000000'
    # Convert query to row arrays
 
    
    return j

    