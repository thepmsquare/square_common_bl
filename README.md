# square_common_bl

## about

common business layer for my personal server.

## Installation

```shell
pip install square_common_bl
```

## env

- python>=3.12.0

## changelog

### v1.9.0

- add authentication -> get_user_details_v0.

### v1.8.0

- add authentication -> update_password_v0.

### v1.7.0

- add authentication -> update_username_v0.

### v1.6.0

- add authentication -> delete_user_v0.

### v1.5.0

- add authentication -> generate_access_token_v0.

### v1.4.0

- add authentication -> logout v0.

### v1.3.2

- validate extra params in greeting -> create_greeting v0.

### v1.3.1

- accept access_token as header instead of query param in greeting -> create_greeting v0.

### v1.3.0

- add square_authentication_helper as dependency.
- replace user_id with access_token in greeting -> create_greeting.

### v1.2.0

- initialize SquareDatabaseHelper in configuration.py.
- remove app_id from greeting -> create_greeting.

### v1.1.0

- add utils -> get_app_id_v0.

### v1.0.0

- initial implementation.

## Feedback is appreciated. Thank you!