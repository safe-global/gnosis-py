from eth.constants import SECPK1_N
from eth_typing import ChecksumAddress, HexAddress, HexStr

NULL_ADDRESS: ChecksumAddress = ChecksumAddress(HexAddress(HexStr("0x" + "0" * 40)))
SENTINEL_ADDRESS: ChecksumAddress = ChecksumAddress(
    HexAddress(HexStr("0x" + "0" * 39 + "1"))
)

# keccak('Transfer(address,address,uint256)')
ERC20_721_TRANSFER_TOPIC: HexStr = HexStr(
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
)

SIGNATURE_R_MIN_VALUE: int = 1
SIGNATURE_R_MAX_VALUE: int = SECPK1_N - 1
SIGNATURE_S_MIN_VALUE: int = 1
SIGNATURE_S_MAX_VALUE: int = SECPK1_N // 2
SIGNATURE_V_MIN_VALUE: int = 27
SIGNATURE_V_MAX_VALUE: int = 28


GAS_CALL_DATA_ZERO_BYTE = 4
GAS_CALL_DATA_BYTE = 16  # 68 before Istanbul
