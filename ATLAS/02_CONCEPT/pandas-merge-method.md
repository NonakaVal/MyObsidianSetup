---
tags:
  - learning/review
HUB:
  - "[[hub-python]]"
  - "[[hub-tratamento-de-dados]]"
---
[[pandas-merge]]
- merge() method 'how' - left and right
```python
# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')
# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right')
```

- right on é o método que define a coluna chave que será usada para a junção das tabelas
```python
# Use right join to merge the movie_to_genres and pop_movies tables

genres_movies = movie_to_genres.merge(pop_movies, 
                                      left_on='movie_id', 
                                      right_on='id', 
                                      how='right')
```

-  Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
```python
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1', '_2'))
```

-  Self join
```python
# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner', suffixes=('_dir','_crew'))

```