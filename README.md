# Prefect Integrations

Show case of buttons trigger pipeline and monitor executions in Prefect.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Self-hosted Prefect Server

```bash
$ prefect server start

 ___ ___ ___ ___ ___ ___ _____ 
| _ \ _ \ __| __| __/ __|_   _| 
|  _/   / _|| _|| _| (__  | |  
|_| |_|_\___|_| |___\___| |_|  

Configure Prefect to communicate with the server with:

    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

View the API reference documentation at http://127.0.0.1:4200/docs

Check out the dashboard at http://127.0.0.1:4200
```

Set server communication

```bash
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
```

## Examples

### With Streamlit

```bash
streamlit run ./WithStreamlit/example.py
```

Goto http://localhost:8501 and press button

### With Flask

```bash
python ./WithFlask/app.py
```

Goto http://127.0.0.1:5000/ and press button

## Resources

- [PrefectHQ/prefect: Prefect is a workflow orchestration tool empowering developers to build, observe, and react to data pipelines](https://github.com/PrefectHQ/prefect)

## Trouble Shooting

- [task - TypeError: 'fn' must be callable (Prefect - Python) - Stack Overflow](https://stackoverflow.com/questions/75107741/typeerror-fn-must-be-callable-prefect-python)

Some resource on the internet might use Prefect V1.0 syntax, be careful.
