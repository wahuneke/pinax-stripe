import stripe

from . import charges
from .. import utils


def create(charge, amount=None, stripe_account=None):
    """
    Creates a refund for a particular charge

    Args:
        charge: the charge against which to create the refund
        amount: how much should the refund be, defaults to None, in which case
                the full amount of the charge will be refunded
        stripe_account: if the Charge was created through Connect, then the connect Account
                        must be provided here
    """
    params = {
        charge: charge.stripe_id,
        stripe_account: stripe_account,
    }

    if amount is not None:
        params['amount'] = \
            utils.convert_amount_for_api(charges.calculate_refund_amount(charge, amount=amount), charge.currency)

    stripe.Refund.create(**params)
    charges.sync_charge_from_stripe_data(charge.stripe_charge, stripe_account=stripe_account)
