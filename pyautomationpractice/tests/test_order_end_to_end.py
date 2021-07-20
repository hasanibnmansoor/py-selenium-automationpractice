import time
import pytest
from pyautomationpractice import logger
from pyautomationpractice.utilities.page_init import init


def test_order_end_to_end(pyf_driver, pyf_username, pyf_password):
    logger.info(
        "[TEST BEGIN] Test to verify end-to-end Product Order Placement of 27 $ Women Dress"
    )

    # Instantiate Page Objects
    page_objects = init(pyf_driver)

    # Step 1: Go to Women Section
    page_objects.home.go_to_women_section()

    # Step 2: get num of colors of 27 dollar products
    num_colors = page_objects.women.num_of_colors_for_27_dollar_product()

    # Step 3: Check for Number of Colors. If more than 1, view details and change color there.
    # Else, Tap Add to Cart.
    if num_colors > 1:
        page_objects.women.view_details_of_27_dollar_product()
        page_objects.productdetails.change_color_and_add_to_cart()
    else:
        page_objects.women.add_27_dollar_product_to_cart()
    
    # Step 4: Proceed to Checkout from Cart Modal
    page_objects.cartmodal.proceed_to_checkout()

    # Step 5: Proceed to Checkout from Cart Summary Page
    page_objects.cartsummary.proceed_to_checkout()

    # Step 6: Login with valid username and password
    page_objects.auth.sign_in(username=pyf_username, password=pyf_password)

    # Step 7: Proceed to Checkout from Address Page, 
    # followed by Shipping Page (accept Terms and Condition)
    page_objects.address.proceed_to_checkout()
    page_objects.shipping.proceed_to_checkout()

    # Step 8: Make Payment by Bankwire and Verify Order is Successful.
    assert page_objects.payment.pay_by_bankwire_and_confirm_order_placed()

    logger.info("[TEST COMPLETED] Test to verify end-to-end Product Order Placement of 27 $ Women Dress")
