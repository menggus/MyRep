from stark.service.stark import site, StarkConfig
from .models import User

site.registry(User)

