from django.core.management import call_command
import pytest

from usaspending_api.accounts.models import AppropriationAccountBalances
from usaspending_api.awards.models import (FinancialAccountsByAwards, FinancialAccountsByAwardsTransactionObligations,
                                           Award, Procurement, FinancialAssistanceAward)
from usaspending_api.financial_activities.models import FinancialAccountsByProgramActivityObjectClass
from usaspending_api.references.models import LegalEntity, Location
from usaspending_api.submissions.models import SubmissionAttributes


@pytest.mark.django_db
def test_load_submission_command():
    """
    Test the submission loader to validate the ETL process
    """
    call_command('loaddata', 'endpoint_fixture_db')
    call_command('load_submission', '-1', '--delete', '--test')
    assertEqual(SubmissionAttributes.objects.all().count(), 1)
    assertEqual(AppropriationAccountBalances.objects.all().count(), 1)
    assertEqual(FinancialAccountsByProgramActivityObjectClass.objects.all().count(), 10)
    assertEqual(FinancialAccountsByAwards.objects.all().count(), 11)
    assertEqual(FinancialAccountsByAwardsTransactionObligations.objects.all().count(), 11)
    assertEqual(Location.objects.all().count(), 4)
    assertEqual(LegalEntity.objects.all().count(), 2)
    assertEqual(Award.objects.all().count(), 7)
    assertEqual(Procurement.objects.all().count(), 1)
    assertEqual(FinancialAssistanceAward.objects.all().count(), 1)
