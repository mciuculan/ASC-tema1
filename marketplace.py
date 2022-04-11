"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Lock


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """

        self.producer_lock, self.cart_lock = Lock(), Lock()

        self.queue_size_per_producer, self.producer_index, self.cart_index, self.shopping_list, \
            self.producer_list = queue_size_per_producer, -1, -1, [], []

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        with self.producer_lock:
            # cresc indexul curent pentru noul producator si-i adaug o lista goala
            self.producer_index += 1
            self.producer_list.append([])
        return self.producer_index

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        no_published_products = len(self.producer_list[producer_id])
        # returneaza fals daca se atinge limita maxima de produse publicate
        if no_published_products < self.queue_size_per_producer:
            # se adauga in lista producatorului elementul cerut
            with self.producer_lock:
                self.producer_list[producer_id].append(product)
                self.producer_index += 1
            return True
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.cart_lock:
            # cresc indexul curent pentru noul cos de cumparaturi si-i adaug o lista goala
            self.cart_index += 1
            self.shopping_list.append([])
        return self.cart_index

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        searched_list = self.producer_list
        for i, _ in enumerate(searched_list):
            for prod in searched_list[i]:
                # se cauta produsul dorit
                if prod[0] is product:
                    with self.cart_lock:
                        # se adauga in cosul cumparatorului
                        self.shopping_list[cart_id].append((prod, i))
                    with self.producer_lock:
                        # se scoate din lista provider-ului
                        searched_list[i].remove(prod)
                    return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        for (elem, producer_index) in self.shopping_list[cart_id]:
            # se cauta elementul dorit
            if elem[0] is product:
                with self.producer_lock:
                    # se pune in lista provider-ului
                    self.producer_list[producer_index].append(elem)
                with self.cart_lock:
                    # se scoate din cosul de cumparaturi
                    self.shopping_list[cart_id].remove((elem, producer_index))
                return

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.shopping_list[cart_id]
