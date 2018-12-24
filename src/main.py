import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import metro_data
import metro_router



def make_time_histogram(line=None):
    """Make a histogram with distribution of links between stations by time."""
    times = []
    for link in metro_data.LINKS:
        if line is None:
            times.append(link[2]['time'])
        elif (metro_data.STATIONS[link[0]]['line'] == line
                and metro_data.STATIONS[link[1]]['line'] == line):
            times.append(link[2]['time'])

    times = np.array(times)
    fig = plt.figure(figsize=(18, 12))
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.hist(times, bins='auto')
    title = 'time distribution ('
    title += ('all' if line is None else 'line ' + str(line)) + ')'
    title += '\n$\mu$ = {0} $\sigma$ = {1}'.format(
            np.around(times.mean(), decimals=2),
            np.around(times.std(), decimals=2))
    plt.title(title, fontsize=42)
    plt.ylabel('number of stations', fontsize=30)
    plt.xlabel('time (in seconds)', fontsize=30)

    try:
        plt.savefig('../img/time_histogram'
                    + ('_all' if line is None else str(line)) + '.pdf',
                    dpi=180, format='pdf')
    except FileNotFoundError:
        print("WARNING! To get a time histogram you should run "
              + "the script 'main.py' inside metro/src/ directory")



def main():
    router = metro_router.Router()
    router.draw_route()
    make_time_histogram()
    make_time_histogram(line=9)

    start_station = metro_router.Station('Верхние Лихоборы')
    finish_station = metro_router.Station('Марксистская')
    route1 = router.make_shortest_route(
            start_station, finish_station,
            is_drawing_graph=True)
    print(route1)

    start_station = metro_router.Station('Фили')
    finish_station = metro_router.Station('Бауманская')
    route2 = router.make_shortest_route(
            start_station, finish_station,
            is_drawing_graph=True)
    print(route2)

    start_station = metro_router.Station('Театральная')
    finish_station = metro_router.Station('Шаболовская')
    intermediate_station1 = metro_router.Station('Улица 1905 года')
    intermediate_station2 = metro_router.Station('Трубная')
    route_with_intermediates = router.make_shortest_route(
            start_station,
            finish_station,
            intermediate_stations=[
                intermediate_station1,
                intermediate_station2
            ],
            is_drawing_graph=True)
    print(route_with_intermediates)



if __name__ == '__main__':
    main()


