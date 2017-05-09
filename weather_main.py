import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    # print the header
    print_the_header()

    # get zipcode from user
    code = input('Waht zipcode do you want the weather for (97201)? ')

    # get html from web
    html = get_html_from_web(code)

    # parse the html
    report = get_weather_from_html(html)

    # display for the forecast
    print('The temp in {} is {}{} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond,
    ))


def print_the_header():
    print('-----------------')
    print('  Learn to Code')
    print('  Weather APP')
    print('-----------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    tempcss = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    tempcss = cleanup_text(tempcss)
    scale = cleanup_text(scale)

    # print(loc, condition, tempcss, scale)

    # return loc, condition, tempcss, scale
    report = WeatherReport(cond=condition, temp=tempcss, scale=scale, loc=loc)
    return report


def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(loc : str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
