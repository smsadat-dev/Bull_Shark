from django.contrib import admin

from .models import (
    CategoryModel, InventoryModel, PurchaseOrderModel, 
    ProductModel, SupplierModel, TransactionModel, WareHouseModel,
    UserAuthProxyModel, 
)

admin.site.index_title = 'Dashboard'
admin.site.site_header = 'Bull Shark dashboard'
admin.site.site_title = 'Dashboard'

admin.site.register(CategoryModel)
admin.site.register(InventoryModel)
admin.site.register(ProductModel)
admin.site.register(PurchaseOrderModel)
admin.site.register(SupplierModel)
admin.site.register(TransactionModel)
admin.site.register(WareHouseModel)
admin.site.register(UserAuthProxyModel)