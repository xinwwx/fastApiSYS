import pandas as pd
import tushare as ts

# 设置tushare pro的token
ts.set_token('你的tushare token')

# 初始化tushare pro
pro = ts.pro_api()

# 获取所有股票的基本信息
stocks = pro.stock_basic()

# 筛选出A股市场的股票
stocks = stocks[stocks['market'] == '主板']

# 选取市值排名前20%的股票
market_cap_rank = stocks.sort_values('total_mv', ascending=False)['ts_code'][:int(len(stocks)*0.2)]

# 选取近三年净利润增长率排名前20%的股票
income = pro.income(ts_code=','.join(stocks['ts_code']), start_date='20180101', end_date='20211231',
                    fields='ts_code,end_date,n_income').groupby('ts_code').sum()
income_growth_rate = (income['n_income'].pct_change(periods=4*3) + 1).groupby('ts_code').prod()
income_growth_rate_rank = income_growth_rate.sort_values(ascending=False)[:int(len(stocks)*0.2)]

# 选取近三年ROE排名前20%的股票
balancesheet = pro.balancesheet(ts_code=','.join(stocks['ts_code']), start_date='20180101', end_date='20211231',
                                fields='ts_code,end_date,roe').groupby('ts_code').mean()
roe_rank = balancesheet.sort_values('roe', ascending=False)[:int(len(stocks)*0.2)]

# 选取市盈率（PE）排名前20%的股票
daily_basic = pro.daily_basic(ts_code=','.join(stocks['ts_code']), trade_date='20220214', fields='ts_code,pe')
pe_rank = daily_basic.dropna().sort_values('pe')[:int(len(stocks)*0.2)]

# 选取20日均线上穿60日均线的股票
ma20 = pro.daily(ts_code=','.join(stocks['ts_code']), start_date='20220126', end_date='20220214',
                 fields='ts_code,trade_date,ma20').groupby('ts_code').mean()
ma60 = pro.daily(ts_code=','.join(stocks['ts_code']), start_date='20220126', end_date='20220214',
                 fields='ts_code,trade_date,ma60').groupby('ts_code').mean()
cross_up = ma20['ma20'] > ma60['ma60']
cross_up_rank = cross_up[cross_up].index.tolist()

# 综合排名
# 综合排名
rank = pd.DataFrame({
    'market_cap_rank': market_cap_rank,
    'income_growth_rate_rank': income_growth_rate_rank.index,
    'roe_rank': roe_rank.index,
    'pe_rank': pe_rank['ts_code'],
})
rank['score'] = rank.apply(lambda x: x.rank().sum(), axis=1)
rank = rank.sort_values('score')[:int(len(stocks)*0.2)]
rank = rank.index.tolist()

# 输出最终筛选出的股票
selected_stocks = list(set(cross_up_rank).intersection(rank))
print(selected_stocks)
