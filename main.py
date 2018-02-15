import skafossdk as Skafos
import turicreate as tc
import pandas as pd


if __name__ == "__main__":
  skafos = Skafos()
  
  skafos.engine.create_view(
        "ratings", {"keyspace": "ea28b544e93cff97e42b770e",
                    "table": "votes"}, DataSourceType.Cassandra).result()

  ratings = pd.DataFrame.from_records(skafos.engine.query("select * from ratings").result()['data'])
  sf = tc.SFrame(data=ratings)
  print(sf, flush=True)
