from hexbytes import HexBytes

# Entrypoint v0.6.0 and v0.7.0 deposited event
# Deposited (index_topic_1 address account, uint256 totalDeposit)
DEPOSIT_EVENT_TOPIC = HexBytes(
    "0x2da466a7b24304f47e87fa2e1e5a81b9831ce54fec19055ce277ca2f39ba42c4"
)

# Safe > 1.4.1 event
# ExecutionFromModuleSuccess (index_topic_1 address module)
EXECUTION_FROM_MODULE_SUCCESS_TOPIC = HexBytes(
    "0x6895c13664aa4f67288b25d7a21d7aaa34916e355fb9b6fae0a139a9085becb8"
)
