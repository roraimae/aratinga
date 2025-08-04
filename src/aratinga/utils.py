def clean_filters(filters):
    filters = {k: v for k, v in filters.items() if v}
    return filters