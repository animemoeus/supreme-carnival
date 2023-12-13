from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.utils import RajaOngkir
from destination.serializers import CheckDestinationSerializer


class CheckDestinationView(GenericAPIView):
    serializer_class = CheckDestinationSerializer

    def get(self, request):
        search = request.query_params.get("search", None)
        raja_ongkir = RajaOngkir()

        if not search:
            return Response(
                {"data": raja_ongkir.get_all_city()},
                status=status.HTTP_400_BAD_REQUEST,
            )

        raja_ongkir = RajaOngkir()

        if raja_ongkir.search_city(search):
            return Response(
                {"data": raja_ongkir.search_city(search)},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"message": f"{search.capitalize()} is not available for destination."},
            status=status.HTTP_400_BAD_REQUEST,
        )
