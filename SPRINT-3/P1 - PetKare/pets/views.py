from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Pet
from groups.models import Group
from traits.models import Trait
from .serializers import PetSerializer


class PetView(APIView, PageNumberPagination):
    def get(self, request: Request) -> Response:
        trait = request.query_params.get("trait", None)
        pets = Pet.objects.all()

        if trait:
            pets = pets.filter(traits__name__iexact=trait.lower())
        
        result_page = self.paginate_queryset(pets, request)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        group_list = serializer.validated_data.pop("group")
        traits_list = serializer.validated_data.pop("traits")

        group_object = Group.objects.filter(
            scientific_name__iexact=group_list["scientific_name"].lower()
        ).first()

        if not group_object:
            group_object = Group.objects.create(**group_list)

        pet_object = Pet.objects.create(
            **serializer.validated_data, group=group_object
            )

        for traits_dict in traits_list:
            traits_object = Trait.objects.filter(
                name__iexact=traits_dict["name"].lower()
                ).first()
            if not traits_object:
                traits_object = Trait.objects.create(**traits_dict)

            pet_object.traits.add(traits_object)

        serializer = PetSerializer(pet_object)

        return Response(serializer.data, status.HTTP_201_CREATED)


class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group", None)
        traits_data = serializer.validated_data.pop("traits", [])

        pet.traits.clear()

        for trait_data in traits_data:
            trait, _ = Trait.objects.update_or_create(
                name__iexact=trait_data["name"],
                defaults=trait_data
            )
            pet.traits.add(trait)

        if group_data:
            group, _ = Group.objects.update_or_create(
                scientific_name__iexact=group_data["scientific_name"],
                defaults=group_data
            )
            pet.group = group

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)
        pet.save()

        serializer = PetSerializer(pet)

        return Response(serializer.data)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)