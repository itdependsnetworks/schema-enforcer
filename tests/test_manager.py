import pytest
import os
from schema_enforcer.schemas.manager import SchemaManager
from schema_enforcer import config

import pdb

FIXTURES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "test_instances")

CONFIG_DATA = {
    "main_directory": os.path.join(FIXTURES_DIR, "schema"),
    "data_file_search_directories": [os.path.join(FIXTURES_DIR, "hostvars")],
    "schema_mapping": {"dns.yml": ["schemas/dns_servers"]},
}

config.load(config_data=CONFIG_DATA)

LOADED_DATA = config.SETTINGS


@pytest.fixture
def schema_manager(scope="module"):
    return SchemaManager(LOADED_DATA)

def test_create_schema_from_file(schema_manager):
    expected_result = 'PASS'
    created_schema = schema_manager.create_schema_from_file(FIXTURES_DIR + "/schema/schemas/", "dns.yml")
    schema_result = created_schema.check_if_valid()[0].result
    assert expected_result == schema_result

def test_iter_schemas(schema_manager):
    expected_schemas = ['schemas/dns_servers', 'schemas/syslog_servers', 'schemas/ntp']
    schemas = schema_manager.iter_schemas()
    for schema in schemas:
        assert schema[0] in expected_schemas

def test_print_schemas(schema_manager):
    pass

def test_test_schemas(schema_manager):
    pass

def test_test_schema_invalid(schema_manager):
    pass

def test_generate_invalid_tests_expected(schema_manager):
    pass

#a = schema_manager()
#b = a.create_schema_from_file(FIXTURES_DIR + "/schema/schemas/", "dns.yml")
#pdb.set_trace()   