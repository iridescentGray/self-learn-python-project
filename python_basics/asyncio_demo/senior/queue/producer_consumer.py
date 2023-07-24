import asyncio
from asyncio import Queue
from random import sample, randint
from typing import List


class Product:

    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:

    def __init__(self, customer_id, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def consumer_customer_queue(queue: Queue, cashier_id: int):
    while not queue.empty():
        customer: Customer = await queue.get()
        for product in customer.products:
            print(
                f"Cashier {cashier_id} Clearing customer {customer.customer_id} 的商品: {product.name} 预计耗时{product.checkout_time}")
            await asyncio.sleep(product.checkout_time)
        queue.task_done()


async def main():
    customer_queue = Queue()
    all_products = [Product("apple", 2), Product("banana", .5),
                    Product("strawberry", 1), Product("Blueberries", .2)]
    for i in range(1, 5):
        products = sample(all_products, randint(2, 4))
        await customer_queue.put(Customer(i, products))
    # Create Cashier
    cashiers = [asyncio.create_task(consumer_customer_queue(customer_queue, i)) for i in range(1, 2)]
    await asyncio.gather(customer_queue.join(), *cashiers)


asyncio.run(main())
