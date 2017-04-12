import pandas as pd

if __name__ == '__main__':

    df = pd.read_json('stream_twt.json')
    del df['entities']                      # Remove this comment once you re-stream the data
    del df['created_at']                    # Remove this comment once you re-stream the data

    count = 0
    for i in df['place']:
        df['place'][count] =  i['full_name']
        count += 1

    df = df[df.lang == 'en']
    df = df.reset_index(drop=True)
    # print(df['id_str'])
    df.to_csv('tweetsDB.csv', encoding = 'utf-8')


    # Ignore warning "A value is trying to be set on a copy of a slice from a DataFrame" if any