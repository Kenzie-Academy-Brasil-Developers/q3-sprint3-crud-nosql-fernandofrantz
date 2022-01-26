def post_route(app):

    @app.post("/posts")
    def create_post():
        from app.controllers.post_controller import create_post
        return create_post()

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        from app.controllers.post_controller import delete_post
        return delete_post(id)

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        from app.controllers.post_controller import get_post_by_id
        return get_post_by_id(id)

    @app.get("/posts")
    def read_posts():
        from app.controllers.post_controller import get_posts
        return get_posts()

    @app.patch("/posts/<int:id>")
    def update_post(id):
        from app.controllers.post_controller import update_post
        return update_post(id)