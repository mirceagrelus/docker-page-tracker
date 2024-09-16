Sample Flask app.
https://realpython.com/docker-continuous-integration/#reader-comments

===
Starting and stopping the server can cause the web page to display an "Access to 127.0.0.1 was denied" error. You can close the socket in chrome:

chrome://net-internals/#sockets

# == Tools ==
```
pylint - flags code style issues
python -m pylint src/
```

```
isort - ensures that your import statements stay organized according to the official recommendation (https://peps.python.org/pep-0008/#imports)
python -m isort src/ --check
python -m isort src/
```

```
black - flags formatting inconsistencies in code
python -m black src/ --check
python -m black src/
```

```
flake8 - check for any other PEP 8 style violations
python -m flake8 src/
```

```
bandit - check for any security issues
python -m bandit -r src/
```