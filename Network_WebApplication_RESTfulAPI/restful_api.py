from flask import Flask, request
# Extension to build RESTful API at ease
from flask_restful import Resource, Api, abort

app = Flask(__name__)
# Declares Api instance using app as argument
api = Api(app)


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TO_DOS:
        abort(404, message=f'Todo {todo_id} doesn\'t exist')


# Inherit from Resource - it manages responses and HTTP codes
class Todo(Resource):
    """
    Shows a single item and lets you add and delete an item.
    """

    def get(self, todo_id=''):
        abort_if_todo_doesnt_exist(todo_id)

        # Return values are: response, http status code, headers
        # Default HTTP code is 200
        return {
                   todo_id: TO_DOS[todo_id],
               }, 200  # {'Etag': 'some-opaque-string'}

    def post(self, todo_id):
        TO_DOS[todo_id] = request.json['data']

        return {
                   todo_id: TO_DOS[todo_id],
               }, 201

    def put(self, todo_id):
        TO_DOS[todo_id] = request.form['data']

        return {
                   todo_id: TO_DOS[todo_id],
               }, 201

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TO_DOS[todo_id]
        return '', 204


class TodoList(Resource):
    """
    Shows a list of all items.
    """

    def get(self):
        return TO_DOS


# Route the resource to a URI. Many endpoints can be routed to the same
# resource.
api.add_resource(TodoList, '/')
api.add_resource(Todo, '/<string:todo_id>')  # , 'endpoint_2)

if __name__ == '__main__':
    TO_DOS = {}
    app.run(host='127.0.0.1', port=5000, debug=True)
