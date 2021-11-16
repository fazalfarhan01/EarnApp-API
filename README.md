# EarnApp API

A Python binding to interact with Earnapp dashboard API.

## Installation
```BASH
pip install pyEarnapp
```
## Usage
```PYTHON
from pyEarnapp import EarnApp
AUTH = "YOUR_AUTH_CODE_FROM_EARNAPP_DASHBOARD"

api = EarnApp(AUTH) # Initiallise the EarnApp object
```
### Functions
1. Get information about the user.
    ```PYTHON
    get_user_data()
    ```
    - Returns an object of type `UserData` with the following attributes.
    ```TXT
    first_name
    last_name
    name
    email
    ```

2. Get information on user's earnings.
    ```PYTHON
    get_earning_info()
    ```
    - Returns an object of type `EarningInfo` with the following attributes.
    ```PYTHON
    balance
    earnings_total
    multiplier
    tokens
    redeem_details
    ```

3. Get all the connected device's information.
    ```PYTHON
    get_devices_info()
    ```
    - Returns an object of type `DevicesInfo` with the following attributes.
    ```PYTHON
    devices # List of nodes connected with each node of object type "Device"
    windows_devices
    linux_devices
    other_devices
    ```
    - The `devices` attribute is a list of devices with each device of object type `Device`.
    - The object `Device` has the following attributes.
    ```PYTHON
    uuid
    bandwidth_usage
    total_bandwidth
    redeemed_bandwidth
    rate
    country
    device_type
    ```
4. Get a list of all the transactions.
    ```PYTHON
    get_transaction_info()
    ```
    - Returns an object of type `Transactions` with the following attributes.
    ```PYTHON
    transactions # List of all transactions
    pending_payments
    paid
    total_transactions
    ```
    - The attribute `transactions` is a list of all transactions with each item of object type `Transaction`.
    - The `Transaction` object has the following attributes.
    ```PYTHON
    uuid
    status
    payment_method
    payment_date
    amount
    payout_date
    is_paid
    ```

5. Add new node/device to your ID.
    ```PYTHON
    add_new_device("EARNAPP_NODE_ID")
    ```
    - Returns the response from the server on success. Else raise an exception.

### Exceptions
The following exceptions are defined.
Exception | Reason
--- | ---
`AuthenticationError` | Raised on authentication failure.
`DeviceAddError` | When the attempt to add device is failed.
`DeviceNotFoundError` | When the device to be added is **not found**.
`DeviceAlreadyAddedError` | When the device ID is already linked
`UnKnownDeviceAddError` | When cause of failure is not known.
`TooManyRequestsError` | Raised when earnapp rate limit is reached.