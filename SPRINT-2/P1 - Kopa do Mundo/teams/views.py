from django.shortcuts import render
from teams.models import Team
from utils import data_processing
from exceptions import (
    NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError)
from rest_framework.views import APIView, status, Response
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)

        return Response(teams_dict, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data_processing(request.data)
        except (
                NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
               ) as error:
            return Response({"error": error.args[0]}, status=status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status=status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status=status.HTTP_200_OK)

    def patch(self, request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status=status.HTTP_200_OK)

    def delete(self, request, team_id: int):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
