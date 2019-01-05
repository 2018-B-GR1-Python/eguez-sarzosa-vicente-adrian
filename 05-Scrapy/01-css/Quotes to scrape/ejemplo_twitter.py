import twitter

api = twitter.Api(consumer_key="OJx1KY5ODi5MAxq6fDWRYFaDQ",
                          consumer_secret="XM4RpNhQAhciaM0SIPAvoWhyS3WjFDmS7zVwrHiAykRabrYHzH",
                          access_token_key="67497207-VPp9nfpxfMwMRZJZQIaGNb2qXAgLoSZVcVGWOce2T",
                          access_token_secret="dJuICTq80nRO8uvvKU6spol0hApbD2HArnXz6vRW3sCkO")

results = api.GetSearch(raw_query="q=#amigo")
print(results)
