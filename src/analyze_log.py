from collections import Counter
from src.importer.csv_importer import CsvImporter
from src.exporter.txt_exporter import TxtExporter


def get_data_by_person(customer, data):
    return [item for item in data if item["customer"] == customer]


def get_most_ordered(customer_data):
    orders_list = [item["order"] for item in customer_data]
    most_common_order = Counter(orders_list).most_common()
    return most_common_order[0][0]


def get_quantity_ordered(customer_data, order_name):
    orders_list = [item["order"] for item in customer_data]
    counter = Counter(orders_list)
    return counter[order_name]


def get_never_ordered(data, customer_data):
    all_orders = set([item["order"] for item in data])
    customer_orders = set([item["order"] for item in customer_data])
    return all_orders.difference(customer_orders)


def get_days_never_went(data, cutomer_data):
    all_days = set([item["day"] for item in data])
    customer_days = set([item["day"] for item in cutomer_data])
    return all_days.difference(customer_days)


def analyze_log(path_to_file):
    data = CsvImporter.import_data(path_to_file)

    maria_data = get_data_by_person("maria", data)
    arnaldo_data = get_data_by_person("arnaldo", data)
    joao_data = get_data_by_person("joao", data)

    most_ordered_maria = get_most_ordered(maria_data)
    qty_hamburguer_arnaldo = get_quantity_ordered(arnaldo_data, "hamburguer")
    never_ordered_joao = get_never_ordered(data, joao_data)
    days_never_went_joao = get_days_never_went(data, joao_data)

    TxtExporter.export_data(
        "data/mkt_campaign.txt",
        [
            most_ordered_maria,
            qty_hamburguer_arnaldo,
            never_ordered_joao,
            days_never_went_joao,
        ],
    )


analyze_log("data/orders_1.csv")
