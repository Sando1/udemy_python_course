import web

render = web.template.render('views/')

urls = (
    '/', 'home'
)

#classes/routes
class home:
    def GET(self):
        return render.home()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
