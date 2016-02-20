from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, ModelResource, fields
from flask_potion.routes import ItemRoute

app = Flask(__name__)
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    done = db.Column(db.Boolean(), nullable=False, default=False)

db.create_all()


class TaskResource(ModelResource):
    class Meta:
        model = Task

    @ItemRoute.PUT('', rel='update')
    def put(self, task, properties):
        return self.manager.update(task, properties)

    put.response_schema = put.request_schema = fields.Inline('self', patchable=True)


api = Api(app)
api.add_resource(TaskResource)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)