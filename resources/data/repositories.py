from resources.data.models import Resource
from resources.business.dtos import ResourceDTO

def create_resource(dto: ResourceDTO):
    resource = Resource.objects.create(
        name=dto.name,
        type=dto.type,
        status=dto.status
    )
    return resource
