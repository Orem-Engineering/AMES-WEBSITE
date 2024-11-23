from django.contrib import admin

# Register your models here.
from django.contrib import admin
from baseapp.models import Constitution
from baseapp.models import Inqury
from baseapp.models import SecondHomepagePicture
from baseapp.models import ThirdHomepagePicture
from baseapp.models import FirstHomepagePicture


# Register your models here.
admin.site.register(Constitution)
admin.site.register(Inqury)
admin.site.register(ThirdHomepagePicture)
admin.site.register(SecondHomepagePicture)
admin.site.register(FirstHomepagePicture)


