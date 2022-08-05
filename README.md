# Djangoproject
python -m venv inmar_envi
C:\Users\FL_LPT-596\Documents\INMAR\inmar_envi\Scripts>activate

pip install -r requirements.txt
django-admin.exe startproject inmarproj .
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py startapp metadata



#shell creation:
----------------
from metadata.models import *
from datetime import datetime

date_value = datetime.now()
Location.objects.create(name = "Perimeter",created_on = date_value, updated_on = date_value )
Location.objects.create(name = "Center",created_on = date_value, updated_on = date_value )

center_loc = Location.objects.get(name = "Center")
perimeter_loc = Location.objects.get(name = "Perimeter")


Department.objects.create(name = "Bakery", location = perimeter_loc ,created_on = date_value, updated_on = date_value )
Department.objects.create(name = "Dairy", location = center_loc ,created_on = date_value, updated_on = date_value )
Department.objects.create(name = "Frozen", location = center_loc ,created_on = date_value, updated_on = date_value )

bakery_dep = Department.objects.get(name = "Bakery")
dairy_dep = Department.objects.get(name = "Dairy")
frozen_dep = Department.objects.get(name = "Frozen")


Category.objects.create(name = "Bakery Bread", location = perimeter_loc, department = bakery_dep ,created_on = date_value, updated_on = date_value )
Category.objects.create(name = "In Store Bakery", location = perimeter_loc, department = bakery_dep ,created_on = date_value, updated_on = date_value )
Category.objects.create(name = "Cheese", location = center_loc, department = dairy_dep ,created_on = date_value, updated_on = date_value )
Category.objects.create(name = "Cream or Creamer", location = center_loc, department = dairy_dep ,created_on = date_value, updated_on = date_value )
Category.objects.create(name = "Frozen Bake", location = center_loc, department = frozen_dep ,created_on = date_value, updated_on = date_value )

bakery_cat = Category.objects.get(name = "Bakery Bread")
instore_cat = Category.objects.get(name = "In Store Bakery")
cheese_cat = Category.objects.get(name = "Cheese")
creamer_cat = Category.objects.get(name = "Cream or Creamer")
frozen_bake_cat = Category.objects.get(name = "Frozen Bake")


SubCategory.objects.create(name = "Bagels", location = perimeter_loc, department = bakery_dep , category = bakery_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Baking or Breading Products", location = perimeter_loc, department = bakery_dep , category = bakery_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "English Muffins or Biscuits", location = perimeter_loc, department = bakery_dep , category = bakery_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Flatbreads", location = perimeter_loc, department = bakery_dep , category = bakery_cat ,created_on = date_value, updated_on = date_value )

SubCategory.objects.create(name = "Breakfast Cake or Sweet Roll", location = perimeter_loc, department = bakery_dep , category = instore_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Cakes", location = perimeter_loc, department = bakery_dep , category = instore_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Pies", location = perimeter_loc, department = bakery_dep , category = instore_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Seasonal", location = perimeter_loc, department = bakery_dep , category = instore_cat ,created_on = date_value, updated_on = date_value )

SubCategory.objects.create(name = "Cheese Sauce", location = center_loc, department = dairy_dep , category = cheese_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Specialty Cheese", location = center_loc, department = dairy_dep , category = cheese_cat ,created_on = date_value, updated_on = date_value )


SubCategory.objects.create(name = "Dairy Alternative Creamer", location = center_loc, department = dairy_dep , category = creamer_cat ,created_on = date_value, updated_on = date_value )

SubCategory.objects.create(name = "Bread or Dough Products Frozen", location = center_loc, department = frozen_dep , category = frozen_bake_cat ,created_on = date_value, updated_on = date_value )
SubCategory.objects.create(name = "Breakfast Cake or Sweet Roll Frozen", location = center_loc, department = frozen_dep , category = frozen_bake_cat ,created_on = date_value, updated_on = date_value )



postgres=# SELECT version();
                          version
------------------------------------------------------------
 PostgreSQL 14.4, compiled by Visual C++ build 1914, 64-bit
(1 row)