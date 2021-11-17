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

    - The object `Device` has the following attributes.

        Attribute | Description
        --- | ---
        `uuid` | UUID of the device.
        `bandwidth_usage` | Unredeemed bandwidth usage.
        `total_bandwidth` | Total bandwindth usage.
        `redeemed_bandwidth` | Redeemed bandwidth usage.
        `rate` | Price/GB of the device.
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
        `payment_date` | Date of payment.
        `amount` | Amount redeemed.
        `redeem_date` | Date on which balance was redeemed.
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
    ```TXT
    referrals
    referral_earnings
    total_referral_earnings
    number_of_referrals
    ```
    - The attribute referrals is a list of all the referrals with each object of type `Referee`.
    - The `Referee` object has the following attributes.
    ```TXT
    id
    bonuses
    bonuses_total
    email
    ```

---

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