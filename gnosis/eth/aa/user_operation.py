import dataclasses
from typing import Any, Dict, Union

from eth_typing import ChecksumAddress, HexStr
from hexbytes import HexBytes


@dataclasses.dataclass
class UserOperation:
    """
    EIP4337 UserOperation
    """

    sender: ChecksumAddress
    nonce: int
    init_code: bytes
    call_data: bytes
    call_gas_limit: int
    verification_gas_limit: int
    pre_verification_gas: int
    max_fee_per_gas: int
    max_priority_fee_per_gas: int
    paymaster_and_data: bytes
    signature: bytes
    entry_point: ChecksumAddress
    transaction_hash: bytes
    block_hash: bytes
    block_number: int
    user_operation_hash: bytes

    def __init__(
        self,
        user_operation_hash: Union[HexStr, bytes],
        user_operation_response: Dict[str, Any],
    ):
        self.sender = ChecksumAddress(
            user_operation_response["userOperation"]["sender"]
        )
        self.nonce: int = int(user_operation_response["userOperation"]["nonce"], 16)
        self.init_code: bytes = HexBytes(
            user_operation_response["userOperation"]["initCode"]
        )
        self.call_data: bytes = HexBytes(
            user_operation_response["userOperation"]["callData"]
        )
        self.call_gas_limit: int = int(
            user_operation_response["userOperation"]["callGasLimit"], 16
        )
        self.verification_gas_limit: int = int(
            user_operation_response["userOperation"]["verificationGasLimit"], 16
        )
        self.pre_verification_gas: int = int(
            user_operation_response["userOperation"]["preVerificationGas"], 16
        )
        self.max_fee_per_gas: int = int(
            user_operation_response["userOperation"]["maxFeePerGas"], 16
        )
        self.max_priority_fee_per_gas: int = int(
            user_operation_response["userOperation"]["maxPriorityFeePerGas"], 16
        )
        self.paymaster_and_data: bytes = HexBytes(
            user_operation_response["userOperation"]["paymasterAndData"]
        )
        self.signature: bytes = HexBytes(
            user_operation_response["userOperation"]["signature"]
        )
        self.entry_point: ChecksumAddress = ChecksumAddress(
            user_operation_response["entryPoint"]
        )
        self.transaction_hash: bytes = HexBytes(
            user_operation_response["transactionHash"]
        )
        self.block_hash: bytes = HexBytes(user_operation_response["blockHash"])
        self.block_number: int = int(user_operation_response["blockNumber"], 16)
        self.user_operation_hash = HexBytes(user_operation_hash)

    def __str__(self):
        return f"User Operation sender={self.sender} nonce={self.nonce} hash={self.user_operation_hash.hex()}"
