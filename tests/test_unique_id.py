from unittest.mock import patch

from phub_python_shared.unique_id import generate_unique_id


@patch('phub_python_shared.unique_id.uuid4', spec=True)
def test_generate_unique_id(m_uuid4):
    m_uuid4.return_value = "generated-unique-id"
    # TESTING
    assert generate_unique_id() == "generated-unique-id"
