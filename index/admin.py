from django.contrib import admin
from index.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_tel', 'user_email']
    list_filter = ['user_id', 'user_name', 'user_tel', 'user_email']
    search_fields = ['user_id', 'user_name', 'user_tel', 'user_email']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'device_name', 'device_pic', 'device_type', 'specifications', 'device_model',
                    'warranty_date', 'purchase_date', 'registry_date', 'location', 'supplier', 'status', 'comment', 'belong']
    list_filter = ['device_id', 'device_name', 'device_pic', 'device_type', 'specifications', 'device_model',
                    'warranty_date', 'purchase_date', 'registry_date', 'location', 'supplier', 'status', 'comment', 'belong']
    search_fields = ['device_id', 'device_name', 'device_pic', 'device_type', 'specifications', 'device_model',
                    'warranty_date', 'purchase_date', 'registry_date', 'location', 'supplier', 'status', 'comment', 'belong']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['belong', 'belong_contact', 'comment']
    list_filter = ['belong', 'belong_contact', 'comment']
    search_fields = ['belong', 'belong_contact', 'comment']


class BorrowAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'user', 'lend_time', 'pre_return', 'return_time', 'reason']
    list_filter = ['device_id', 'user', 'lend_time', 'pre_return', 'return_time', 'reason']
    search_fields = ['device_id', 'user', 'lend_time', 'pre_return', 'return_time', 'reason']


class RepairAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'repair_time', 'repair_man', 'repair_money', 'repair_num', 'comment']
    list_filter = ['device_id', 'repair_time', 'repair_man', 'repair_money', 'repair_num', 'comment']
    search_fields = ['device_id', 'repair_time', 'repair_man', 'repair_money', 'repair_num', 'comment']


class ScrapAdmin(admin.ModelAdmin):
    list_display = ['device_id', 'scrap_reason', 'available_year', 'comment']
    list_filter = ['device_id', 'scrap_reason', 'available_year', 'comment']
    search_fields = ['device_id', 'scrap_reason', 'available_year', 'comment']


admin.site.register(User, UserAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(BorrowManage, BorrowAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Scrap, ScrapAdmin)
admin.site.register(Repair, RepairAdmin)
