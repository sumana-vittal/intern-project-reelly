from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By



@when("Click on 'off plan' at the left side menu.")
def click_off_plan(context):
    context.app.off_plan.click_off_plan()

@when("Click on the first product.")
def click_first_product(context):
    context.app.off_plan.click_first_product()

@then("Verify the product page is loaded")
def verify_product_page_loaded(context):
    context.app.off_plan.verify_product_page_loaded()

@then("Verify the three options of visualization are 'architecture', 'interior', 'lobby'")
def verify_visualization(context):
    context.app.off_plan.verify_visualization()

@then("Verify the visualization options are clickable.")
def verify_visualization_clickable(context):
    context.app.off_plan.verify_visualization_options_clickable()
