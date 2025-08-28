def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price
try:
    original_price = float(input("Enter the original price: "))
    discount_rate = float(input("Enter the discount percentage: "))

    # Call the function to get the final price
    final_price = calculate_discount(original_price, discount_rate)

    # Print the result
    print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter valid number")