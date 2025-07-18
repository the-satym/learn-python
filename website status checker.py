import requests
from requests import Response

def get_response(url: str) -> Response:
    return requests.get(url)

def show_reponse(response: Response) -> None:
    print(f'status code: {response.status_code}')
    print(f'content type: {response.headers["content-type"]}')
    print(f' encoding: {response.encoding}')
    print(f'is redirected: {response.is_redirect}')
    print(f'history: {response.history}')
    print(f'cookies: {response.cookies}')
    print(f'elapsed time: {response.elapsed}')
    print(f'links: {response.links}')
    print(f'ok: {response.ok}')
    print(f'is permanent redirect: {response.is_permanent_redirect}')


def main() -> None:
    url: str = input('Enter a url: ')
    response: Response = get_response(url)
    show_reponse(response)








if __name__ == '__main__':
    main()