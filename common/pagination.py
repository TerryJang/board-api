

class OffsetPagination:

    def __init__(self, model, queryset, size, page):
        self.model = model
        self.queryset = queryset
        self.size = size
        self.page = page

    def get_has_prev_page(self, first_id):
        if self.queryset.filter(self.model.id < first_id).first() is not None:
            return True
        return False

    def get_has_next_page(self, last_id):
        if self.queryset.filter(self.model.id > last_id).first() is not None:
            return True
        return False

    def paginate(self):
        offset = (self.page - 1) * 10

        result = self.queryset.offset(offset).limit(self.size).all()

        pagination = {
            "total_count": self.queryset.count(),
            "has_prev_page": self.get_has_prev_page(result[0].id),
            "has_next_page": self.get_has_next_page(result[-1].id),
            "current_page": self.page,
            "current_count": len(result),
        }

        return pagination, result

class CursorPagination:
    pass
