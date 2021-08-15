from flask import request

class BasePagination:
    '''
    queryset should be model.query object
    model should contain to_json() method.
    '''
    page = 1
    page_size = 5

    def __init__(self, queryset) -> None:
        self.url = request.url
        self.page_num = int(request.args.get("page",self.page))
        self.page_size_num = int(request.args.get("page_size",self.page_size))
        self.pagination = queryset.paginate(self.page_num, per_page= self.page_size_num, error_out=False)

    def previous_url(self):
        if not self.pagination.has_prev:
            return None
        return self.url.replace("page="+str(self.page_num), "page="+str(self.pagination.prev_num))
    
    def next_url(self):
        if not self.pagination.has_next:
            return None
        if "page" not in request.args:
            if request.args:
                return self.url+"&page=2"
            else:
                return self.url+"?page=2"
        return self.url.replace("page="+str(self.page_num), "page="+str(self.pagination.next_num))

    def to_json(self):
        return {
            "count":self.pagination.total,
            "previous": self.previous_url(),
            "next": self.next_url(),
            "result": [item.to_json() for item in self.pagination.items]
        }