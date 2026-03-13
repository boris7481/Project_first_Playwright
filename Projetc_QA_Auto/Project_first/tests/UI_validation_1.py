import time

from playwright.sync_api import Page, expect, Playwright


# this fonction is for the login the site
def test_UIValidationDynamicScript(page: Page):
    page.goto("https://www.automationexercise.com/signup")
    page.get_by_role("button", name="Einwilligen").click()
    page.locator('[data-qa="login-email"]').fill("junior74814615@gmail.com")
    page.locator('[data-qa="login-password"]').fill("09w0823@Junior ")
    page.locator('[data-qa="login-button"]').click()
    blue_top = page.locator(".product-image-wrapper").filter(has_text="Blue Top").first
    blue_top.hover()
    blue_top.locator(".add-to-cart").first.click()

#    blue_top.locator(".fa fa-shopping-cart").filter(has_text="Add to cart").click()
#    blue_top.get_by_role("button", name="Add to cart").click()
#    blue_top.locator(".btn btn-default add-to-cart").click()


#    page.locator('[data-qa="login-button"]').click()
#    Blue_Top = page.locator(".productinfo text-center").filter(has_text="Blue Top").hover()
#    Blue_Top.get_by_role("button", name="Add to cart")

#    Men_shirt = page.locator(".features_items").filter(has_text="Men Tshirt")
#    Men_shirt.get_by_role("button", name="Add to cart")
#    page.get_by_role( "button", name="Cart").click()
#    time.sleep(10)
##    page.get_by_role("button", name="Continue Shopping").click()
