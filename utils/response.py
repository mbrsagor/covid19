def prepare_create_success_response():
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Data Successfully created'
    }
    return response


def prepare_user_create_success(message):
    response = {
        "status": True,
        "message": message
    }
    return response


def prepare_user_create_failed():
    response = {
        "status": False,
        "message": "User not created success."
    }
    return response


def prepare_success_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Data successfully returned',
        'data': serializer_data
    }
    return response


def profile_success_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': 'Profile successfully returned',
        'profile': serializer_data
    }
    return response


def prepare_success_delete_response(serializer_data):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'code': 204,
        'data': serializer_data
    }
    return response


def prepare_success_res(message):
    response = {
        'status': True,
        'message': message
    }
    return response


def prepare_error_response(message):
    """ prepare error response for all serializer """
    response = {
        'status': False,
        'message': message
    }
    return response


def prepare_detail_response(serializer):
    response = {
        "status": True,
        "message": "Data successfully returned",
        "details": serializer
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
        "status": False,
        "message": details,
        "data": None
    }
    return response

