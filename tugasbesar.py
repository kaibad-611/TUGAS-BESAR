class Product:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

def bubble_sort_products(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j].harga > products[j + 1].harga:
                products[j], products[j + 1] = products[j + 1], products[j]
    return products

def display_products_table(products):
    print("-" * 30)
    print("| {:15} | {:10} |".format("Nama Produk", "harga"))
    print("-" * 30)
    for product in products:
        print("| {:15} | {:10.2f} |".format(product.nama, product.harga))
    print("-" * 30)

products = [
    Product("Laptop", 8800000.00),
    Product("Smartphone", 2599000.00),
    Product("Television", 1155000.00),
    Product("Headphone", 1769000.00),
    Product("Kulkas", 1500000.00),
    Product("Air Conditioner", 3250000.00),
    Product("Kompor Listrik", 999000.00),
    Product("Rice Cooker", 2199000.00),
    Product("Mesin Cuci", 3499000.00),
    Product("Microwave", 1499000.00),
]

print("Produk Sebelum di setting :")
display_products_table(products)

sorted_products = bubble_sort_products(products)

print("\nProduk setelah di seting dari harga terendah:")
display_products_table(sorted_products)
