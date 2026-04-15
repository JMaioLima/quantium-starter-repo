from app import app
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


# Test 1: Header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualisation" in header.text


# Test 2: Visualisation is present
def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


# Test 3: Region picker is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None