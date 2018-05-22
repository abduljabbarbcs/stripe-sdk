from stripe_sdk.config import Config as cfg


class StripeSdk:

    def __init__(self):
        print("stripe sdk")

    @staticmethod
    def set_api_key(api_key):
        cfg.STRIPESDK.api_key = api_key

    @staticmethod
    def get_api_key(api_key):
        return cfg.STRIPESDK.api_key

    @staticmethod
    def create_customer(token, email=None):
        try:
            customer = cfg.STRIPESDK.Customer.create(
                description="Customer for " + email,
                source=token  # obtained with Stripe.js
            )
            return customer
        except Exception as e:
            return e

    @staticmethod
    def retrieve_customer(customer_id):
        try:
            customer = cfg.STRIPESDK.Customer.retrieve(
                customer_id
            )
            return customer
        except Exception as e:
            return e

    @staticmethod
    def create_product(name, type='service'):
        try:
            product =cfg.STRIPESDK.Product.create(
              name=name,
              type=type,
            )
            return product
        except Exception as e:
            return e

    @staticmethod
    def create_plan(product_id, plan_name, amount, interval='month',currency='usd'):
        try:
            plan = cfg.STRIPESDK.Plan.create(
              currency=currency,
              interval=interval,
              product=product_id,
              nickname=plan_name,
              amount=amount,
            )
            return plan
        except Exception as e:
            return e

    @staticmethod
    def create_subscription(customer_id, plan_id, coupon_id=None):
        try:
            if coupon_id:
                subscription = cfg.STRIPESDK.Subscription.create(
                  customer=customer_id,
                  items=[{'plan': plan_id}],
                  coupon=coupon_id,
                )
            else:
                subscription = cfg.STRIPESDK.Subscription.create(
                    customer=customer_id,
                    items=[{'plan': plan_id}],
                )
            return subscription
        except Exception as e:
            return e

    @staticmethod
    def create_coupon(percent_off):
        try:
            coupon = cfg.STRIPESDK.Coupon.create(
              percent_off=percent_off,
              duration="forever",
            )
            return coupon
        except Exception as e:
            return e

    @staticmethod
    def get_product(id):
        try:
            product = cfg.STRIPESDK.Product.retrieve(id=id)
            return product
        except Exception as e:
            return e

    @staticmethod
    def get_plans(id):
        try:
            plans = cfg.STRIPESDK.Plan.all(product=id)
            return plans
        except Exception as e:
            return e
