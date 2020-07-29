---
title: Pandas cheatsheets
created: '2020-07-29T11:23:41.327Z'
modified: '2020-07-29T14:42:04.141Z'
---

# Pandas cheatsheets

## Data description
```python
df.columns                       # get column names 
df[['name1', 'name2', 'name3']]  # select columns 
```

## General queries
```python
df.groupby('TempChamber','Freq')['VCC'].count() #counte number of unique VCC + Freq + TampChamber
selection = df.loc[(df[Freq] == 5920) & (df[TempChamber] == 25)  & (df[DSA_raw] == 0) & (df[V_in] == 9)];
```

