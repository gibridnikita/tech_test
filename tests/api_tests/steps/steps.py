from behave import when, then

from tests.api_tests.controllers.airport_controller import AirportController
from tests.api_tests.utils.json_validator import validate_json_schema


@when('user navigates to airports page')
def get_airports_page(context):
    context.response = AirportController().get_airports()
    context.response_json = context.response.json()


@when('user calculates distance between "{first_airport}" and "{second_airport}" airports')
def calculate_distance_between_airports(context, first_airport, second_airport):
    payload = {
        "from": first_airport,
        "to": second_airport,
    }
    context.response = AirportController().calculate_distance(payload)
    context.response_json = context.response.json()


@then('the response status code should be {expected_status}')
def check_status_code(context, expected_status):
    actual_status = context.response.status_code
    assert actual_status == int(
        expected_status), f"Expected status code {expected_status} is not equals to current {actual_status}"


@then('the response should match the "{schema_file}" schema')
def validate_schema_file(context, schema_file):
    validate_json_schema(context.response.json(), schema_file)


@then('the response should contain {expected_count} airports')
def validate_airports_count(context, expected_count):
    actual_count = len(context.response_json['data'])
    assert actual_count == int(
        expected_count), f"Expected airports count {expected_count} is not equals to current {actual_count}"


@then('the following airports should be in the response')
def validate_airports_in_response(context):
    expected_airports = [row['airports'] for row in context.table]
    actual_airports = [airport['attributes']['name'] for airport in context.response_json['data']]
    for expected_airport in expected_airports:
        assert expected_airport in actual_airports, (
            f"Expected airport '{expected_airport}' not found in response. "
            f"Actual airports: {actual_airports}"
        )


@then('the distance between airports should be greater than {distance} km')
def varify_distance(context, distance):
    distance_between_airports = context.response_json['data']['attributes']['kilometers']
    assert distance_between_airports > int(
        distance), f"Distance between airports {distance_between_airports} km is equal or less than {distance} km."