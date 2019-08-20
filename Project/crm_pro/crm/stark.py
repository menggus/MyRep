from stark.service.stark import StarkConfig, site
from crm.models import Department


class DepartConfig(StarkConfig):
    list_display = []


site.register(Department)
