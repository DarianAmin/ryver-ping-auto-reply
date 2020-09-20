# Ryver Ping Auto Reply

Ryver bot to automatically send replies to pings and PM the exact contents of the message you were pinged in.

## Getting started

### Clone this repository
To clone the repository, simply run this command in your preferred terminal:

```sh
$ git clone https://github.com/DarianAmin/ryver-ping-auto-reply.git
```

Now, navigate into this new directory:

```sh
$ cd ryver-ping-auto-reply
```

### Installing dependencies
The bot currently has one dependency, [`pyryver`](https://pypi.org/project/pyryver/). Install it with the following command:

```sh
$ pip install --upgrade pyryver
```

### Adding your Ryver login
In the `main.py` file, you'll need to replace `Organization_Name`, `Username`, and `Password` with their respective values.

For example, if you typically log into Ryver at `acme.ryver.com` with the username `important_ceo` and the password `password123`, these three values will be `acme`, `important_ceo`, and `password123` respectively.
