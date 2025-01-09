from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .validators import validate_branch_name, validate_owner_id
from .models import Branch
from rest_framework.exceptions import ValidationError

# Create your views here.
class BranchView(APIView):
    def post(self, request):
        try:
            branch_name = request.data.get("branchName")
            owner_id = request.data.get("ownerId")
            validate_branch_name(branch_name)
            owner = validate_owner_id(owner_id)
        
            branch = Branch.objects.create(
                name=branch_name,
                owner=owner
            )

            print("Created branch", branch)
            return Response(
                {"message": "Branch created successfully"}, status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
