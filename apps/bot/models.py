from django.db import models


class TelegramUser(models.Model):
    join_date = models.DateTimeField(auto_now_add=True, verbose_name='Joined at')
    user_id = models.BigIntegerField(unique=True, verbose_name='user_id')
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name='username')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last name')

    is_banned = models.BooleanField(default=False, verbose_name='Is Banned')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Balance')
    subscription_status = models.BooleanField(default=False, verbose_name='Subscription status')
    subscription_expiration = models.DateTimeField(blank=True, null=True, verbose_name='Subscription expiration')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    class Meta:
        db_table = 'telegram_users'
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        ordering = ['user_id']


class TelegramReferral(models.Model):
    referrer = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='given_referrals')
    referred = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='received_referrals')
    level = models.IntegerField(default=0, verbose_name='Level')

    def __str__(self):
        return f"{self.referrer} {self.referrer}"

    class Meta:
        unique_together = ('referrer', 'referred')


class TelegramBot(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name='Username')
    title = models.CharField(max_length=255, verbose_name='Title', blank=True, null=True)
    token = models.CharField(max_length=255, verbose_name='Token', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        db_table = 'telegram_bots'
        verbose_name = 'Telegram Bot'
        verbose_name_plural = 'Telegram Bots'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Transaction(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    currency = models.CharField(max_length=100, blank=True, null=True, verbose_name='Currency')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"Transaction of {self.user.username}: {self.amount} at {self.timestamp}"


class VpnKey(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Key')
    is_limit = models.BooleanField()
    data_limit = models.IntegerField(verbose_name='Data Limit GB')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    def __str__(self):
        return f"{self.key} ({self.created_at})"


class Server(models.Model):
    hosting = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Hosting')
    ip_address = models.CharField(max_length=1000, blank=True, null=True, verbose_name='IP Address')
    user = models.CharField(max_length=1000, blank=True, null=True, default='root', verbose_name='user')
    password = models.CharField(max_length=1000, blank=True, null=True, default='<PASSWORD>', verbose_name='password')
    configuration = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Configuration')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Rental Price')
    max_keys = models.IntegerField(blank=True, null=True, verbose_name='Max Keys')
    keys_generated = models.IntegerField(blank=True, null=True, verbose_name='Keys')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')

    api_url = models.CharField(max_length=1000, blank=True, null=True, verbose_name='API URL')
    cert_sha256 = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Certificate SHA256')
    script_out = models.TextField(blank=True, null=True, verbose_name='Script Out Info JSON')

    def __str__(self):
        return f"{self.ip_address} {self.hosting} ({self.created_at})"


class GlobalSettings(models.Model):
    server_amount = models.IntegerField(blank=True, null=True, verbose_name='Server Amount')
    time_web_api_key = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Time Web API')
    payment_system_api_key = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Payment System 1')


class ReferralSettings(models.Model):
    level_1_percentage = models.IntegerField(blank=True, null=True, verbose_name='Level 1 Percentage')
    level_2_percentage = models.IntegerField(blank=True, null=True, verbose_name='Level 2 Percentage')
    level_3_percentage = models.IntegerField(blank=True, null=True, verbose_name='Level 3 Percentage')
    level_4_percentage = models.IntegerField(blank=True, null=True, verbose_name='Level 4 Percentage')
    level_5_percentage = models.IntegerField(blank=True, null=True, verbose_name='Level 5 Percentage')

    def __str__(self):
        return f"Level 1 {self.level_1_percentage}% Level 2 {self.level_2_percentage}% Level 3 {self.level_3_percentage}% Level 4 {self.level_4_percentage}% Level 5 {self.level_5_percentage}%"


class IncomeInfo(models.Model):
    total_amount = models.IntegerField(blank=True, null=True, verbose_name='Amount Total')
