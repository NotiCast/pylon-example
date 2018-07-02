import click
import requests

API_URL = ("https://5vl5kit83e.execute-api.us-east-1.amazonaws.com/test/send_m"
           "essage")


# Use this in your code to easily send a NotiCast message!
def send_message(message, api_key, api_url):
    data = {"message": message}
    headers = {"X-API-Key": api_key}
    requests.post(api_url, json=data, headers=headers)


@click.command()
@click.option("--api_url", default=API_URL, help="NotiCast API URL")
@click.argument("api_key")
@click.argument("message")
def main(message, api_key, api_url):
    send_message(message, api_key, api_url)
    data = {"message": message}
    headers = {"X-API-Key": api_key}
    print(data)
    print(requests.post(api_url, json=data, headers=headers))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
