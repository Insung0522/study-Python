import pandas as pd
import matplotlib.pyplot as plt
import pymssql

# MSSQL 데이터베이스 연결 설정
server = '192.168.0.10:1433'
user = 'balecalc2'
password = 'balecalc'
database = 'Moist_HS_DJ'
# 데이터베이스 연결
conn = pymssql.connect(server, user, password, database)
# 각 센서 데이터 가져오기
query_s1 = "SELECT [id], [s1_len] FROM [Moist_HS_DJ].[dbo].[s1_sensor]"
query_s2 = "SELECT [id], [s2_len] FROM [Moist_HS_DJ].[dbo].[s2_sensor]"
query_s3 = "SELECT [id], [s3_len] FROM [Moist_HS_DJ].[dbo].[s3_sensor]"
query_s4 = "SELECT [id], [s4_len] FROM [Moist_HS_DJ].[dbo].[s4_sensor]"
query_s5 = "SELECT * FROM [Moist_HS_DJ].[dbo].[s5_sensor]"

df_s1 = pd.read_sql(query_s1, conn)
df_s2 = pd.read_sql(query_s2, conn)
df_s3 = pd.read_sql(query_s3, conn)
df_s4 = pd.read_sql(query_s4, conn)
df_s5 = pd.read_sql(query_s5, conn)
df = [df_s1, df_s2, df_s3, df_s4, df_s5]

# 데이터베이스 연결 종료
conn.close()


# 서브플롯 생성 (2행 3열 구조, 마지막 하나는 빈 공간)
fig, axs = plt.subplots(2, 3, figsize=(16, 7))

# 그래프 그리기 함수
def draw_graph(ax, df, cnt):
    idx = 's' + str(cnt) + '_len'
    ax.plot(df['id'], df[idx], linestyle="-", color='#4A82BD')
    ax.set_title(idx)
    # ax.set_xlabel('No')
    # ax.set_ylabel(idx)
    ax.grid(True)

    ax.set_xticks(range(0, len(df['id']), 50)) # x축 간격 50씩
    # ax.set_yticks(range(0, 3500, 250))
                  
# 각 데이터프레임에 대해 그래프 그리기
for cnt, (ax, df) in enumerate(zip(axs.flat, df), start=1):
    draw_graph(ax, df, cnt)

# 빈 공간 제거
fig.delaxes(axs[1, 2])

# 레이아웃 조정
plt.tight_layout()
plt.show()