"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self)
        self.carts, self.marketplace, self.retry_wait_time, self.cart_index, self.name = \
            carts, marketplace, retry_wait_time, marketplace.new_cart(), kwargs['name']

    def run(self):
        for cart in self.carts:
            for operation in cart:
                # pentru fiecare operatie din fiecare cos, verificam tipul ei
                if operation['type'].__eq__('add'):
                    count = 0
                    while count < operation['quantity']:
                        # se adauga in cos pana se ajunge la cantitatea ceruta
                        # se asteapta daca nu este valabil
                        attempt = self.marketplace.add_to_cart(self.cart_index,
                                                               operation['product'])
                        if attempt:
                            count += 1
                        else:
                            sleep(self.retry_wait_time)
                elif operation['type'].__eq__('remove'):
                    count = 0
                    while count < operation['quantity']:
                        # se scoate cantitatea ceruta din cos
                        self.marketplace.remove_from_cart(self.cart_index, operation['product'])
                        count += 1
                else:
                    raise NotImplementedError("No such operation type")

        for product, _ in self.marketplace.place_order(self.cart_index):
            print(f"{self.name} bought {product[0]}")
