from pyEarnapp import EarnApp
AUTH_TOKENS = [
    "1%2F%2F0dKMJwG9ekzH1CgYIARAAGA0SNwF-L9Ir3TbDTUaua2-8KR7IWQd7Jr7AwIB1XFNGyWLXhYVXi30xy84m5JklfkOjzT3xMQloKS8",
    "1%2F%2F0dahtCNwckwNECgYIARAAGA0SNgF-L9IrV6aIVrOfyz-IYo-OD9ew7oQ5Mn2k0IgSRdOcZzNjhnU7oP-b8H2rN7qDKaeG6d7XkA",
    "1%2F%2F0dtI2hxltQ6iPCgYIARAAGA0SNwF-L9IrrCqtZoZeEH6Tsg9uG8KaDHwz6N1tFTBbUl4EE9gheb-6VhUWxqvQrcCcN2qW34TUJzo"
]

for auth in AUTH_TOKENS:
    api = EarnApp(auth)
    devices_info = api.get_devices_info()
    for device in devices_info.devices:
        print(device.uuid, device.banned.is_banned)
