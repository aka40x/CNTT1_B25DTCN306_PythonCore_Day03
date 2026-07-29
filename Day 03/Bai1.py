inventory = [
    {"id": "SP1", "name": "Tai nghe Sony", "price": 1200000, "category": "Phụ kiện"},
    {"id": "SP2", "name": "Chuột không dây", "price": 450000, "category": "Phụ kiện"},
    {"id": "SP3", "name": "Bàn phím Cơ", "price": 950000, "category": "Phụ kiện"},
    {"id": "SP4", "name": "Màn hình Dell 27 inch", "price": 4500000, "category": "Thiết bị"},
    {"id": "SP5", "name": "Sạc dự phòng 20000mAh", "price": 350000, "category": "Phụ kiện"}
]


def linear_search_filter(cart, target_category, max_price):
    result = []
    for product in cart:
        if product["price"] <= max_price and product["category"] == target_category:
            result.append(product)
    return result


def print_filter_result(result, target_category, max_price):
    print("KẾT QUẢ LỌC SẢN PHẨM (LINEAR SEARCH MULTI-CRITERIA)")
    print(f"Danh mục tìm kiếm: {target_category} | Giá tối đa: {max_price:,} VNĐ")
    print(f"Tìm thấy {len(result)} sản phẩm phù hợp:")
    for product in result:
        print(f"  -> [{product['id']}] {product['name']} | Giá: {product['price']:,} VNĐ")


if __name__ == "__main__":
    filtered_products = linear_search_filter(inventory, "Phụ kiện", 1000000)
    print_filter_result(filtered_products, "Phụ kiện", 1000000)