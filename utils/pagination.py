from rest_framework import pagination, response, status
from rest_framework.exceptions import APIException

from utils import messages


class NotFound(APIException):
    status_code = status.HTTP_200_OK
    default_detail = ('bad_request.')
    default_code = 200


class PosPagination(pagination.PageNumberPagination):

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        try:
            self.page = paginator.page(page_number)
        except Exception as exc:
            # Here it is
            msg = {
                'status': 'fail',
                'message': exc,
                'data': []
            }
            # print(NotFound(msg))
            raise NotFound(msg)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    # Customization default response
    def get_paginated_response(self, data):
        next_page = self.get_next_link()
        prev_page = self.get_previous_link()
        if next_page is None and prev_page is None:
            return response.Response({
                'status': 'success',
                'message': messages.DATA_RETURN,
                'data': data
            })
        else:
            return response.Response({
                'status': 'success',
                'message': messages.DATA_RETURN,
                'data': data
            })
