# Notre Dame Women's Basketball Schedule Web Scraper

## How to Use:
```
chmod +x scraper.py
./scraper.py
```
The program prints the game information, including the date, opponent, and location.

The program runs once with one worker and then again with five workers, each time printing the games, game count, and runtime.

The program requires python3 and requests.

## My Scraper in Action:

### One Worker
<img width="498" height="650" alt="image" src="https://github.com/user-attachments/assets/e122a543-89ef-4a17-8d1b-8b490134815c" />

### Five Workers
<img width="499" height="643" alt="image" src="https://github.com/user-attachments/assets/ab475124-db24-4534-ad13-d5a771579fc4" />

## Performance Impact:
### Functional Programming:
The scraper uses map() to apply the game_info function to each individual game. map() simplifies my code and keeps the transformations concise and in one location. map() itself does not run concurrently.
```
map(game_info, data['data'])
```
### Concurrency:
The scraper uses concurrent.futures.ThreadPoolExecutor and executor.map() to request multiple pages concurrently. 

The program runs once with one worker and again with five workers. With five workers, requests can overlap with each other and ultimately reduce the time spent. Both programs returned 30 games, with the one-worker program taking 0.408 seconds and the five-worker program taking 0.09 seconds (4.53 times as fast).
