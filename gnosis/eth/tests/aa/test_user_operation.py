from unittest import TestCase

from gnosis.eth.account_abstraction import UserOperation
from gnosis.eth.tests.mocks.mock_bundler import (
    safe_4337_chain_id_mock,
    safe_4337_user_operation_hash_mock,
    user_operation_mock,
)


class TestUserOperation(TestCase):
    def test_get_user_operation_hash(self):
        user_operation_hash = safe_4337_user_operation_hash_mock.hex()
        user_operation = UserOperation(
            user_operation_hash, user_operation_mock["result"]
        )
        self.assertEqual(
            user_operation.get_user_operation_hash(safe_4337_chain_id_mock),
            safe_4337_user_operation_hash_mock,
        )
