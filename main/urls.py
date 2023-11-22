from django.urls import path
from main.views import show_main
from main.views import show_main, create_product
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

from main.views import register 
# from main.views import login_user
from main.views import logout_user

from main.views import add_stock
from main.views import delete_product
from main.views import subtract_stock
from main.views import edit_product

from main.views import get_product_json
from main.views import add_product_ajax, add_ajax, remove_ajax, remove_all_ajax, create_product_flutter, get_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    # path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-stock/<int:product_id>/', add_stock, name='add_stock'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),
    path('subtract-stock/<int:product_id>/', subtract_stock, name='subtract_stock'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('add-ajax/', add_ajax, name='add_ajax'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
    path('remove-all-ajax/', remove_all_ajax, name='remove_all_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-flutter/', get_flutter, name='get_flutter'),
]