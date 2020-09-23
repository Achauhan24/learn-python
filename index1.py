# import tornado.web
# import tornado.ioloop

# class basicRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world this is a python command executed from BE")

# class listRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html")

# class queryRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         num = self.get_argument("num")
#         if (num.isdigit()):
#             r = "odd" if int(num) %2 else "even"
#             self.write(f"The integer is {r}")
#         else:
#             self.write(f"{num} is not a valid integer")

# class resourceParamRequestHandler(tornado.web.RequestHandler):
#     def get(self, studentName, courseId):
#         self.write(f"Welcome {studentName} the course u r viewing is {courseId}")


# if __name__ == "__main__":
#     app = tornado.web.Application([
#         (r"/", basicRequestHandler),
#         (r"/animal", listRequestHandler),
#         (r"/isEven", queryRequestHandler),
#         (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler)
#     ])

# port = 8882
# app.listen(port)
# print(f"Application is ready and listening on port {port}")

# tornado.ioloop.IOLoop.current().start()