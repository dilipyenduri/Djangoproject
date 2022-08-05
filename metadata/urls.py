from django.conf.urls import url
from django.urls import path

from metadata.views import *

urlpatterns = [
    
    path('v1/location/', LocationData.as_view(), name='LocationData'),
    path('v1/<int:location_delete_id>/location/', LocationData.as_view(), name='LocationDeleteData'),
    path('v1/location/<int:location_id>/department', DepartmentData.as_view(), name='DepartmentDeleteData'),
     path('v1/location/<int:location_id>/<int:dept_delete_id>/department', DepartmentData.as_view(), name='DepartmentData'),
    path('v1/location/<int:location_id>/department/<int:department_id>/category', CategoryData.as_view(), name='CategoryData'),
    path('v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory', SubCategoryData.as_view(), name='SubCategoryData'),
   
    ]

