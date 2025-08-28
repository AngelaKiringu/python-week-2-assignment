def calculate_discount(price, discount_percent):
    """Return final price after discount if discount >= 20%, else original price."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


def main():
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    final_price = calculate_discount(price, discount_percent)

    if final_price == price:
        print(f"No discount applied. Final price: {final_price:.2f}")
    else:
        print(f"Discount applied: {discount_percent:.2f}%")
        print(f"Final price: {final_price:.2f}")


if __name__ == "_main_":
    main()