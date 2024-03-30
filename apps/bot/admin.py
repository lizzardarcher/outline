from django.contrib import admin
from apps.bot.models import TelegramBot, TelegramUser, TelegramReferral, ReferralSettings, GlobalSettings, VpnKey, \
    Server, IncomeInfo, Transaction, Price


# Register your models here.


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = (
        'join_date', 'first_name', 'last_name', 'username', 'subscription_status', 'subscription_expiration')
    search_fields = ('first_name', 'last_name', 'username', 'user_id')
    readonly_fields = ('join_date', 'first_name', 'last_name', 'username',)
    ordering = ('-subscription_status', 'subscription_expiration',)
    empty_value_display = '---'

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('title', 'token', 'username', 'created_at')

    def has_add_permission(self, request):
        if TelegramBot.objects.all():
            return False
        else:
            return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(TelegramReferral)
class TelegramReferralAdmin(admin.ModelAdmin):
    list_display = ('referrer', 'referred', 'level')

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'currency', 'timestamp')

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(ReferralSettings)
class ReferralSettingAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(GlobalSettings)
class GlobalSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(IncomeInfo)
class IncomeInfo(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(VpnKey)
class VpnKey(admin.ModelAdmin):
    list_display = ('user', 'server', 'is_limit', 'data_limit', 'created_at')

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = (
        'hosting', 'ip_address', 'user', 'password', 'rental_price', 'max_keys', 'keys_generated', 'is_active',
        'created_at')


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Price.objects.all():
            return False
        else:
            return True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
