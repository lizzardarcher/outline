from django.contrib import admin
from apps.bot.models import TelegramBot, TelegramUser, TelegramReferral,ReferralSettings,GlobalSettings,VpnKey,Server,IncomeInfo,Transaction
# Register your models here.
admin.site.register(TelegramBot)
admin.site.register(TelegramUser)
admin.site.register(TelegramReferral)
admin.site.register(ReferralSettings)
admin.site.register(Transaction)
admin.site.register(GlobalSettings)
admin.site.register(IncomeInfo)
admin.site.register(VpnKey)
admin.site.register(Server)