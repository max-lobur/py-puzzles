#### Initialzing
```
mkvirtualenv fb-calc --python=python3
pip install -r requirements.txt
```

#### Unit-testing
```
pytest -v
```

#### Testing on a real data:
1. Register a few own test users: [MANUAL](https://developers.facebook.com/docs/apps/test-users)
2. Generate user token with `user_posts` permission for each:
    * In a separate browser window login as test user
    * Go to [API explorer](https://developers.facebook.com/tools/explorer)
    * Get token marking the `user_posts`
3. Write down the `test_data.csv`
4. Run the script:
    ```
    python fb_calc.py test_data.csv
    ```
