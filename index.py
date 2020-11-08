import tornado.web
import tornado.ioloop
import asyncio
import json

class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("list.txt", "r") #reads from a text file
        fruits = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        fh = open("list.txt", "a")
        fh.write(f"{fruit}\n")
        fh.close()
        self.write(json.dumps({"message": "Fruit added successfully"}))

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = tornado.web.Application([
        (r"/", mainRequestHandler),
        (r"/list", listRequestHandler)
    ])

    port = 8882
    app.listen(port)
    print(f"application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
