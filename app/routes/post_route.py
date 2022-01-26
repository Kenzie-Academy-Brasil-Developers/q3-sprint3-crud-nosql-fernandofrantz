def post_route(app):

    @app.post("/posts")
    def create_post():
        from app.controllers.post_controller import create_post
        return create_post()

    @app.delete("/posts/<int:id>")
    def delete_post():
        return ''

    @app.get("/posts/<int:id>")
    def read_post_by_id():
        return ''

    @app.get("/posts")
    def read_posts():
        return ''

    @app.patch("/posts/<int:id>")
    def update_post():
        return ''