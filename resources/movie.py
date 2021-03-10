from flask import Response, request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Movie, User

class MoviesApi(Resource):

    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        movie = Movie(**body, added_by=user)
        movie.save()
        user.update(push__movies=movie)
        user.save()
        id = movie.id
        return make_response(jsonify({'id': str(id)}), 200)

class MovieApi(Resource):

    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        movie.update(**body)
        return make_response('Ok', 200)

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        movie = Movie.objects.get(id=id, added_by=user_id)
        movie.delete()
        return make_response('Ok', 200)

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)
