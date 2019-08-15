from stark.service.stark import site, StarkConfig
from .models import User
from stark.service.combsearce import Option, Row


class DistinctNameOption(Option):

    def get_queryset(self, _field, model_class, query_dict):

        return Row(model_class.objects.filter(**self.condition).values_list('area').distinct(),self,query_dict)


class UserConfig(StarkConfig):

    list_display = [StarkConfig.display_checkbox, "id", "name", "telephone", "area", "level", "depart", StarkConfig.display_edit_del]

    search_field = [
        DistinctNameOption("area", value_func=lambda x:x[0], text_func=lambda x:x[0]),
        Option("depart", is_multi=True),
        Option("level", is_choice=True, text_func=lambda x:x[1])
    ]


site.registry(User, UserConfig)

# # 组合搜索配置. 根据什么进行组合搜索?
#     list_filter = [
#         # DistinctNameOption('name',condition={'id__gt':9},value_func=lambda x:x[0],text_func=lambda x:x[0],),
#         Option('level',is_choice=True,text_func=lambda x:x[1]),
#         Option('user',text_func=lambda x:x.title,is_multi=True),
#         # Option('tel',text_func=lambda x:x.tel),
#         Option('proj',is_multi=True)
#     ] # 配置项多


