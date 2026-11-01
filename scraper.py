#!/usr/bin/env python3

import requests
import concurrent.futures
import re
import json
import time

def game_info(game):
    opponent = game['opponent_name']
    date = re.findall(r'\d{4}-\d{2}-\d{2}', game['datetime'])[0]
    location = game['location']

    return f'{date} | {opponent} | {location}'

def scrape(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    data = response.json()
    return list(map(game_info, data['data']))

def main():
    url = 'https://fightingirish.com/website-api/schedule-events?filter%5Bschedule_id%5D=735&filter%5Bupcoming%5D=true&filter%5Bhide_from_specific_sport_schedule%5D=false&sort=datetime&include=articlesExists,conference.image,opponent.customLogo,opponent.officialLogo,opponentLogo,postEventArticle.image,postScheduleEventPage,preEventArticle.image,preScheduleEventPage,presentedBy,promotionalItems.image,schedule.sport,scheduleEventLinks.icon,scheduleEventResult,scheduleEventTags.image,secondOpponent.customLogo,secondOpponent.officialLogo,secondOpponentLogo,tournament&per_page=6&page='
    urls = [f'{url}{page}' for page in range(1,6)]
    for workers in [1,5]:
        start = time.perf_counter()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor: results = list(executor.map(scrape, urls))
        
        elapsed = time.perf_counter() - start
        count = 0
        for page in results:
            for game in page:
                print(game)
                count += 1

        print(f'\nGames: {count}')
        print(f'Workers: {workers}')
        print(f'Time: {elapsed: .3f} seconds \n')

if __name__ == "__main__":
    main()
