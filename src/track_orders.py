from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        orders_list = [item[1] for item in self.orders if item[0] == customer]
        most_common_order = Counter(orders_list).most_common()
        return most_common_order[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_orders = set([item[1] for item in self.orders])
        customer_orders = set(
            [item[1] for item in self.orders if item[0] == customer]
        )
        return all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        all_days = set([item[2] for item in self.orders])
        customer_days = set(
            [item[2] for item in self.orders if item[0] == customer]
        )
        return all_days.difference(customer_days)

    def count_days(self):
        days_list = [item[2] for item in self.orders]
        most_common_day = Counter(days_list).most_common()
        return most_common_day

    def get_busiest_day(self):
        most_common_day = self.count_days()
        return most_common_day[0][0]

    def get_least_busy_day(self):
        most_common_day = self.count_days()
        return most_common_day[-1][0]
