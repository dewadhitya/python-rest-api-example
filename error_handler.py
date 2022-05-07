from flask import make_response

class AppError:
    def bad_request(self):
        return make_response(
            {"error_msg": "The requirement doesn't fulfilled."},
            400
        )

    def not_found(self):
        return make_response(
            {"error_msg": "the ID does not match!"},
            404
        )