import pandas as pd

if __name__ == '__main__':

    DataFrame = pd.read_json('stream_twt.json')
    del DataFrame['entities']                      # Remove this comment once you re-stream the data
    del DataFrame['created_at']                    # Remove this comment once you re-stream the data

    count = 0

    for i in DataFrame['place']:
        DataFrame['place'][count] =  i['full_name'] # Replaces Long/Lat Coordinates with place name
        count += 1                                  # in example 43.66,73 will now be New York, NY

    DataFrame = DataFrame[DataFrame.lang == 'en']   # returns all enteries with language as english
    DataFrame = DataFrame.reset_index(drop=True)    # re-indexes all the enteries
    # print(df['id_str'])
    DataFrame.to_csv('tweetsDB.csv', encoding = 'utf-8')


    # Ignore warning "A value is trying to be set on a copy of a slice from a DataFrame" if any

