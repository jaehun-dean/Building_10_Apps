from movie_client import MovieClient
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('------------------------')
    print('    Movie Search App')
    print('------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)
                # print(client.perform_search())

                results = client.perform_search()
                print('Found {} results.'.format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                        r.Year, r.Title
                    ))
        except requests.exceptions.ConnectionError:
            print('Error: Cannot search, you network is down.')
        except ValueError as ve:
            print('Error: You search string is invalid: {}'.format(ve))
        except Exception as x:
            print('Error: {}'.format(x))

    print('exiting...')

if __name__ == '__main__':
    main()