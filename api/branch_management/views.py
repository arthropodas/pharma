from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .validators import validate_branch_name, validate_owner_id
from .models import Branch
from rest_framework.exceptions import ValidationError
from api.utils.middlewares import CustomIsAuthenticated
from api.utils.permissions import IsOwner, IsStaff
from api.utils.error_messages import error_code_2003


# Create your views here.
class BranchView(APIView):
    authentication_classes = (CustomIsAuthenticated,)

    def post(self, request):
        try:
            branch_name = request.data.get("branchName")
            validate_branch_name(branch_name)

            branch = Branch.objects.create(name=branch_name, owner=request.user)

            print("Created branch", branch)
            return Response(
                {"message": "Branch created successfully"}, status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BranchGetView(APIView):
    authentication_classes = (CustomIsAuthenticated,)
    permission_classes = (IsOwner,)

    def get(self, request, pk):
        # import pdb;pdb.set_trace()
        try:

            branch = Branch.objects.get(id=pk)

            # Serialize the branch details manually or using a serializer
            data = {
                "id": branch.id,
                "name": branch.name,
                "owner": {
                    "id": branch.owner.id,
                    "name": branch.owner.first_name + " " + branch.owner.last_name,
                    "email": branch.owner.email,
                },
                "pharmacist": {
                    "id": branch.pharmacist.id if branch.pharmacist else None,
                    "firstName": (
                        f"{branch.pharmacist.first_name} {branch.pharmacist.last_name}"
                        if branch.pharmacist
                        else None
                    ),
                    "email": branch.pharmacist.email if branch.pharmacist else None,
                },
            }

            return Response(data, status=status.HTTP_200_OK)

        except Branch.DoesNotExist:
            return Response(error_code_2003(), status=status.HTTP_400_BAD_REQUEST)
