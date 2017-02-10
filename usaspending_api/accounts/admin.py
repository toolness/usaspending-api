from django.contrib import admin

from usaspending_api.accounts.models import (AppropriationAccountBalances,
                                             TreasuryAppropriationAccount)


@admin.register(TreasuryAppropriationAccount)
class TreasuryAppropriationAccountAdmin(admin.ModelAdmin):

    pass


@admin.register(AppropriationAccountBalances)
class AppropriationAccountBalancesAdmin(admin.ModelAdmin):

    pass
