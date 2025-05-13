Feature: Airports API

  Scenario: User is able to navigate to Airports page and see the count of airports
    When user navigates to airports page
    Then the response status code should be 200
    And the response should match the "airports_schema.json" schema
    And the response should contain 30 airports


  Scenario: User is able to verify specific airports
    When user navigates to airports page
    Then the response status code should be 200
    And the following airports should be in the response
      | airports            |
      | Akureyri Airport                |
      | St. Anthony Airport |
      | CFB Bagotville      |


  Scenario: User is able to see distance between airports
    When user calculates distance between "KIX" and "NRT" airports
    Then the response status code should be 200
    And the response should match the "distance_schema.json" schema
    And the distance between airports should be greater than 400 km
