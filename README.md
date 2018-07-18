# BE Test

1. User wants to input daily exchange rate data = url /exrate
2. User has a list of exchange rates to be tracked = url /daterate
3. User wants to add an exchange rate to the list = url /addexrate
4. User wants to remove an exchange rate from the list = url /deleterate


# Prepare  :

Build the images:
```
$ docker-compose -f docker-compose-dev.yml build
```
Run the containers:
```
$ docker-compose -f docker-compose-dev.yml up -d
```

Create the database:
```
$ docker-compose -f docker-compose-dev.yml \
  run users python manage.py recreate_db
```
Seed the database:
```
$ docker-compose -f docker-compose-dev.yml \
  run users python manage.py seed_db
```
# input_field :
```
rate_from
rate_to
rate_date
rate
```

# DB : 

| Schema |   Name    | Type  |  Owner       |
|--------|-----------|-------|----------    |
| public | listrates | table | postgres     |
| public | rates     | table | postgres     |

```
 select * from listrates;
```

  | id | rate_from | rate_to |      rate_date          |
  | ---|-----------|---------|---------------------    |
  |  2 | EUR       | USD     | 2018-07-15 00:00:00     |
  |  3 | USD       | IDR     | 2018-07-15 00:00:00     |
  |  4 | GBP       | JPY     | 2018-07-15 00:00:00     |
  |  5 | HKS       | USD     | 2018-07-17 00:00:00     |
  |  6 | IDR       | USD     | 2018-07-17 00:00:00     |
(5 rows)

```
select * from rates;
```

| id | rate_from | rate_to |  rate   |      rate_date         |
|----|-----------|---------|---------|---------------------   |
|  1 | EUR       | IDR     | 1029139 | 2018-07-15 00:00:00    |
|  2 | EUR       | USD     | 10293   | 2018-07-15 00:00:00    |
|  3 | GBP       | JPY     | 109733  | 2018-07-15 00:00:00    |
|  4 | EUR       | USD     | 109273  | 2018-10-17 00:00:00    |
|  5 | EUR       | USD     | 109273  | 2018-10-17 00:00:00    |
|  6 | USD       | IDR     | 109373  | 2018-10-17 00:00:00    |

(6 rows)