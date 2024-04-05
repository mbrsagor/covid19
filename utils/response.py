from utils import messages


def prepare_create_success_response(message):
    """ prepare success response for all serializer """
    response = {
        'status': 'success',
        'message': message
    }
    return response


def promo_code_validation_response(message, pk, code, discount):
    """ prepare success response for all serializer """
    response = {
        'status': 'success',
        'message': message,
        'id': pk,
        'code': code,
        'discount': discount,

    }
    return response


def prepare_success_response(message):
    """ prepare success response for all serializer """
    response = {
        'status': 'success',
        'message': message
    }
    return response


def prepare_single_success_response(data):
    """Prepare single success response"""
    response = {
        'status': 'success',
        'message': messages.DATA_RETURN,
        'data': data
    }
    return response


def prepare_success_list_response(message, data):
    """ prepare success response for all serializer """
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    return response


def prepare_error_response(serializer_error):
    """ prepare error response for all serializer """
    response = {
        'status': 'fail',
        'message': serializer_error,
    }
    return response


def prepare_generic_error(error_code, details):
    """
    method for build generic error
    @param error_code: error_code should be provided by this param
    @param details: error message
    :return:
    """
    response = {
        'status': 'fail',
        "message": details
    }
    return response
