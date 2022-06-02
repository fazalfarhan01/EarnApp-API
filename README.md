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

### To use API with proxies
```PYTHON
from pyEarnapp import EarnApp
AUTH = "YOUR_AUTH_CODE_FROM_EARNAPP_DASHBOARD"

api = EarnApp(AUTH)
proxy_conf = {
        'http': socks5://username:password@ipaddress:port,
        'https': socks5://username:password@ipaddress:port,
    }
earning_info = api.get_user_data(proxies=proxy_conf)
```

All additional arguements are passed on to the `requests.method` call.

---


### Functions
1. Get information about the user.
    ```PYTHON
    get_user_data()
    ```
    - Returns an object of type `UserData` with the following attributes.

        Attribute | Description
        --- | ---
        `first_name` | User's first name
        `last_name` | User's last name
        `name` | User's full name
        `email` | User's login email


2. Get information on user's earnings.
    ```PYTHON
    get_earning_info()
    ```
    - Returns an object of type `EarningInfo` with the following attributes.

        Attribute | Description
        --- | ---
        `balance` | Current earned balance.
        `earnings_total` | Amount earned till date.
        `multiplier` | Earning multiplier.
        `tokens` | No idea what this is.
        `redeem_details` | Returns object of type `RedeemDetails`.
        `bonuses` | Earnings from referrals.
        `bonuses_total` | Total earnings from referrals till date.
        `referral_part` | Referral bonus percentage.

    - The object `RedeemDetails` has the following attributes.
    
        Attribute | Description
        --- | ---
        `email` | Redemption email
        `payment_method` | Redemption method

3. Get all the connected device's information.
    ```PYTHON
    get_devices_info()
    ```
    - Returns an object of type `DevicesInfo` with the following attributes.
    
        Attribute | Description
        --- | ---
        `devices` | List of nodes connected with each node of object type `Device`.
        `windows_devices` | Number of Windows devices.
        `linux_devices` | Number of Linux devices.
        `other_devices` | Number of other type of devices.
        `total_bandwidth_usage` | Shows bandwidth usage of all devices combined in bytes.
        `total_bandwidth_usage_formatted` | Shows bandwidth usage of all devices combined as friendly string e.g. 2.4GB.

    - The object `Device` has the following attributes.

        Attribute | Description
        --- | ---
        `uuid` | UUID of the device.
        `name` | Name of the device.
        `bandwidth_usage` | Unredeemed bandwidth usage in bytes.
        `bandwidth_usage_formatted` | Unredeemed bandwidth usage as friendly string e.g. 2.4GB.
        `total_bandwidth_usage` | Total bandwidth usage in bytes.
        `total_bandwidth_usage_formatted` | Total bandwidth usage as friendly string e.g. 2.4GB.
        `redeemed_bandwidth` | Redeemed bandwidth usage in bytes.
        `redeemed_bandwidth_formatted` | Redeemed bandwidth usage as friendly string e.g. 2.4GB.
        `rate` | Price/GB of the device.
        `earned` | Unredeemed earnings for this device.
        `earned_total` | Total earnings for this device.
        `country` | Country of the device.
        `device_type` | Type of device. (win/node/`None`)

4. Get a list of all the transactions.
    ```PYTHON
    get_transaction_info()
    ```
    - Returns an object of type `Transactions` with the following attributes.

        Attribute | Description
        --- | ---
        `transactions` | `List` of all transactions with each object of type `Transaction`.
        `pending_payments` | Number of **pending** payments.
        `paid` | Number of payments **completed**. 
        `total_transactions` | Total number of transactions.


    - The `Transaction` object has the following attributes.
        Attribute | Description
        --- | ---
        `uuid` | Transaction ID.
        `status` | Status of transaction (`pending`/`paid`).
        `payment_method` | Mode of payment.
        `payment_date` | Is an object of type `datetime.datetime`, as date of payment.
        `amount` | Amount redeemed.
        `redeem_date` | Is an object of type `datetime.datetime`, as date on which balance was redeemed.
        `is_paid` | `True` if the payment is completed.


5. Add new node/device to your ID.
    ```PYTHON
    add_new_device("EARNAPP_NODE_ID")
    ```
    - Returns the response from the server on success. Else raise an exception.

6. Get a list of all [referrals](https://earnapp.com/i/GBAVJMH) and their bonuses.
    ```PYTHON
    get_referral_info()
    ```
    - Returns an obejct of type `Referrals` with the following attributes.
        Attribute | Description
        --- | ---
        `referrals` | `List` of all the referrals with each object of type `Referee`.
        `referral_earnings` | **Unredeemed** earnings from referrals. (Same as `get_earning_info().bonuses`)
        `total_referral_earnings` | Total earnings from referrals. (Same as `get_earning_info().bonuses_total`)
        `number_of_referrals` | Total number of accepted referrals
    

    - The `Referee` object has the following attributes.
        Attribute | Description
        --- | ---
        `id` | Referral ID.
        `bonuses` | Unredeemed bonus from referred user.
        `bonuses_total` | Total bonus from referred user.
        `email` | Partially hidden referred user's email.

7. Delete linked device
    ```PYTHON
    delete_device(device_uuid = 'sdk-node-adfbafdnbasgnb')
    ```
    - Returns `true` when deleted, else `False`

8. Check if IP Address is usable on earnapp
    ```python
    is_ip_allowed()
    ```
    - Returns `true` if IP Address is allowed, else `false`.

9. Redeem balance to PayPal
    ```python
    redeem_to_paypal(paypal_email = 'someone@example.com')
    ```
    - Returns `true` on successful redeem, else `False`.


---

### Exceptions
- The following exceptions are defined.
    Exception | Reason
    --- | ---
    `AuthenticationError` | Raised on authentication failure.
    `DeviceAddError` | When the attempt to add device is failed.
    `DeviceNotFoundError` | When the device to be added is **not found**.
    `DeviceAlreadyAddedError` | When the device ID is already linked
    `UnKnownDeviceAddError` | When cause of failure is not known.
    `TooManyRequestsError` | Raised when earnapp rate limit is reached.
    `UnKnownIPCheckError` | Raised when there's an error checking if the IP address is valid.
    `InValidIPAddressError` | Raised when the IP address is invalid.
    `UnKnownRedeemError` | When unknown error occurs on redeption.
    `MinimumRedeemBalanceError` | When account doesn't have minimum balance needed for redeeming.
