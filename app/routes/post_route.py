def post_route(app):

    @app.get("/posts")
    def read_posts():
        return ''
