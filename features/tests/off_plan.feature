Feature: Test scenario for off plan

  Scenario: verify the visualization feature of product
    Given Open the main page
    When Click on the sign in
    And Log in to the page.
    And Click on 'off plan' at the left side menu.
    And Click on the first product.
    Then Verify the product page is loaded
    Then Verify the three options of visualization are 'architecture', 'interior', 'lobby'
    And Verify the visualization options are clickable.