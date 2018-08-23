import click
import requests

API_URL = "https://api.noticast.io/send_message"

# Use send_message() in your own code!


@click.command()
@click.option("--api_url", default=API_URL, help="NotiCast API URL")
@click.argument("api_key")
@click.argument("message")
@click.argument("target_arn")
def send_message(message, api_key, api_url, target_arn):
    data = {"message": message, "target": target_arn}
    headers = {"X-API-Key": api_key}
    output = requests.post(api_url, json=data, headers=headers)
    print(output.json())


if __name__ == "__main__":
    send_message()  # pylint: disable=no-value-for-parameter
