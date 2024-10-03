from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата {amount} рублей с помощью кредитной карты выполнена"

class EWalletPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата {amount} рублей с помощью элекронного кошелька выполнена"

class Platform(ABC):
    def __init__(self, paymentmethod: PaymentMethod):
        self.paymentmethod = paymentmethod

    @abstractmethod
    def makepay(self, amount):
        pass

class MobileAppPlatform(Platform):
    def makepay(self, amount):
        return f"Мобильное приложение: {self.paymentmethod.pay(amount)}"

class WebPlatform(Platform):
    def makepay(self, amount):
        return f"Вебсайт: {self.paymentmethod.pay(amount)}"


def scenario(payment_type, platform_type, amount):
    if payment_type == 'c_card':
        paymentmethod = CreditCardPayment()
    elif payment_type == 'e_wallet':
        paymentmethod = EWalletPayment()
    else:
        return "Неизвестный способ оплаты"

    if platform_type == 'mobile':
        platform = MobileAppPlatform(paymentmethod)
    elif platform_type == 'web':
        platform = WebPlatform(paymentmethod)
    else:
        return 'Неизвестная платформа'

    return platform.makepay(amount)

print(scenario("c_card", "mobile", 5000))
print(scenario("e_wallet", "web", 1000))
