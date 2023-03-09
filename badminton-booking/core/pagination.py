
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """
    ?page=all
    For retrieve all list without pagination
    """
    all = 'all'
    page_size_query_param = 'page_size'

    def get_page_size(self, request):
        if request.query_params.get(self.page_query_param) == self.all:
            return None
        return super().get_page_size(request)

