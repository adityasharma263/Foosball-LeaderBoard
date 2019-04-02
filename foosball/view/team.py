from foosball.model.team import Team
from foosball import app
from sqlalchemy import or_
from flask import jsonify, request
from foosball.schema.team import TeamSchema
import datetime
from itertools import cycle
import simplejson as json


@app.route('/api/v1/team', methods=['GET', 'POST'])
def team_api():
    if request.method == 'GET':
        # args = request.args.to_dict()
        # args.pop('page', None)
        # args.pop('per_page', None)
        # page = int(request.args.get('page', 1))
        # per_page = int(request.args.get('per_page', 10))
        score = Team.query.order_by(Team.score.desc()).distinct(Team.score).limit(10).all()[-1].score
        data = Team.query.filter(Team.score >= score).order_by(Team.score.desc()).all()
        # for obj in data:
        #     print(obj.score)
        # data = Team.query.filter_by(**args).max(Team.score).limit(10).all()
        result = TeamSchema(many=True).dump(data)
        return jsonify({'result': {'teams': result.data}, 'message': "Success", 'error': False})
    else:
        post = Team(**request.json)
        post.save()
        result = TeamSchema().dump(post)
        return jsonify({'result': {'team': result.data}, 'message': "Success", 'error': False})


@app.route('/api/v1/team/<int:id>', methods=['PUT', 'DELETE'])
def team_id(id):
    if request.method == 'PUT':
        put = Team.query.filter_by(id=id).update(request.json)
        if put:
            Team.update_db()
            s = Team.query.filter_by(id=id).first()
            result = TeamSchema(many=False).dump(s)
            return jsonify({'result': result.data, "status": "Success", 'error': False})
    else:
        teams = Team.query.filter_by(id=id).first()
        if not teams:
            return jsonify({'result': {}, 'message': "No Found", 'error': True})
        Team.delete_db(teams)
        return jsonify({'result': {}, 'message': "Success", 'error': False})