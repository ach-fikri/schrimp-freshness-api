from fastapi import APIRouter, Response

auth_router = APIRouter()

@auth_router.get('/login')
async def login(request):

    return Response(status_code=200)

