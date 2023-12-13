from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.utils import RajaOngkir
from destination.serializers import CheckDestinationSerializer


class CheckDestinationView(GenericAPIView):
    serializer_class = CheckDestinationSerializer

    def get(self, request):
        search = request.query_params.get("search", None)

        if not search:
            return Response(
                {"message": "`search` params is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        raja_ongkir = RajaOngkir()
        if raja_ongkir.check_city(search):
            return Response(
                {"message": f"{search.capitalize()} is available for destination."},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"message": f"{search.capitalize()} is not available for destination."},
            status=status.HTTP_200_OK,
        )
