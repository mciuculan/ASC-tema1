"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from time import sleep
from threading import Thread


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, group=None, **kwargs)

        self.products, self.marketplace, self.republish_wait_time, self.producer_id,\
            self.product_no = products, marketplace, republish_wait_time,\
                                        marketplace.register_producer(), 0

    def run(self):
        # Cat timp nu s-a ajuns la cantitatea ceruta, se publica produse
        while 1:
            count = 0
            while count < self.products[self.product_no][1]:
                attempt = self.marketplace.publish(self.producer_id,
                                                   self.products[self.product_no])
                if attempt:
                    count += 1
                    sleep(self.products[self.product_no][2])
                else:
                    # se asteapta pana spatiul permite publicarea
                    sleep(self.republish_wait_time)
            number_of_products = len(self.products) - 1
            # daca s-a ajuns la finalul listei, se reseteaza indexul
            if self.product_no is number_of_products:
                self.product_no = 0
            else:
                # altfel creste numarul de produse
                self.product_no += 1
