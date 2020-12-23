import traceback
import sys
import hashlib

from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.exceptions import InternalError
from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.log import init_console_logging

FAMILY_NAME = "iot"

def _hash(data):
    '''Compute the SHA-512 hash and return the result as hex characters.'''
    return hashlib.sha512(data).hexdigest()

# Prefix for iot is the first six hex digits of SHA-512(TF name).
iot_namespace = _hash(FAMILY_NAME.encode('utf-8'))[0:6]

class IoTTransactionHandler(TransactionHandler):

    def __init__(self, namespace_prefix):
        self._namespace_prefix = namespace_prefix

    @property
    def family_name(self):
        return FAMILY_NAME

    @property
    def family_versions(self):
        return ['1.0']

    @property
    def namespaces(self):
        return [self._namespace_prefix]

    def apply(self, transaction, context):                                                
        
        # Get the payload and extract iot-specific information.
        header = transaction.header
        payload_list = transaction.payload.decode().split(",")
        operation = payload_list[0]
        amount = payload_list[1]

        # Get the public key sent from the client.
        from_key = header.signer_public_key

        if operation == "store_sensor_data":
            self._store_sensor_data(context, amount, from_key)

    def _store_sensor_data(self, context, amount, from_key):
        wallet_address = self._get_wallet_address(from_key)

        state_data = str(amount).encode('utf-8')
        addresses = context.set_state({wallet_address: state_data})

        if len(addresses) < 1:
            raise InternalError("State Error")

    def _get_wallet_address(self, from_key):
        return _hash(FAMILY_NAME.encode('utf-8'))[0:6] + _hash(from_key.encode('utf-8'))[0:64]

def main(destino):
    '''Entry-point function for the sensor transaction processor.'''
    try:
        init_console_logging()
        # Register the transaction handler and start it.
        processor = TransactionProcessor(url=destino)
        handler = IoTTransactionHandler(iot_namespace)
        processor.add_handler(handler)
        processor.start()

    except KeyboardInterrupt:
        pass
    except SystemExit as err:
        raise err
    except BaseException as err:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
