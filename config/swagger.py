from drf_spectacular.utils import extend_schema_view, extend_schema


def add_swagger_tag(swagger_tags=None, methods=None):
    """
    Кастомный декоратор для разделения эндпоинтов по блокам в интерфейсе свагера,
    например для случая когда в одном приложении много эндпоинтов

    :param swagger_tags: List of tags to be used for Swagger documentation.
    :param methods: List of HTTP methods (e.g., ['get', 'post', 'put', 'patch', 'delete']).
    """
    if swagger_tags is None:
        swagger_tags = []
    if methods is None:
        methods = ["get", "post", "put", "patch", "delete"]

    # Generate the dictionary for @extend_schema_view
    schema_kwargs = {method: extend_schema(tags=swagger_tags) for method in methods}

    # Return the @extend_schema_view decorator with generated schema_kwargs
    return extend_schema_view(**schema_kwargs)
