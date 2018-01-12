
import web
import json
from database import insert, 
urls = (
'/index', 'index',
'/requestSubmit','requestSubmit',
'/getRequests','getRequests'
)
app = web.application(urls, globals(), autoreload=False)
render = web.template.render('templates/')
class index1:
    def GET(self):
        return render.FeatureRequest()
class requestSubmit:
    def POST(self):
        # Get form data from JSON and insert into Temporary DB
        data = json.loads(web.data())
        return insert(data)
class getRequests:
    def GET(self):
        return getData();
    
if __name__== "__main__":
    app.run()          