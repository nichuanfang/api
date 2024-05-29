# 剧集 处理类
from core import cache
from core.result import Page
from db.turso import acquire_client_sync

# 查询总数
TOTAL_COUNT = 'SELECT COUNT(*) FROM show'
# 分页查询剧集 列表(按照最后观看时间排序)
QUERY_SHOW_BY_PAGED = 'SELECT * FROM show  ORDER BY last_watched_at DESC LIMIT :page_size OFFSET :offset'
# 更新分享链接
UPDATE_SHOW_SHARE_LINK = 'UPDATE show SET share_link = :share_link WHERE show_id = :show_id'
#  根据类型查询索引表数据
SELECT_LOCAL_SEARCH_BY_TYPE = "SELECT * FROM local_search WHERE type = ?"
# 根据show_id查询剧集详情
SELECT_SHOW_BY_ID = "SELECT * FROM show WHERE show_id = ?"


@cache.cache_with_expiry(876000)
def get_shows(curr_page: int = 1, page_size: int = 10):
	"""分页查询剧集列表

	Args:
		curr_page (int, optional): 第几页. 默认1

		page_size (int, optional): 每页多少条数据. 默认10

	Returns:
		_type_: 剧集列表
	"""
	with acquire_client_sync() as turso_client:
		page = Page(curr_page, page_size)
		
		# 查询总数
		total_count: int = turso_client.execute(
			TOTAL_COUNT).rows[0][0]  # type: ignore
		# 设置总页数与总数
		page.set_total_count(total_count)
		if total_count == 0:
			return page
		
		page_data = []
		# 执行查询
		result_set = turso_client.execute(QUERY_SHOW_BY_PAGED, {
			'page_size': page_size, 'offset': (curr_page - 1) * page_size})
		columns = result_set.columns
		for row in result_set.rows:
			data = {}
			for index in range(0, len(columns)):
				# 将查询结果转换为字典
				data[columns[index]] = row[index]
			page_data.append(data)
		page.data = page_data
		return page


@cache.cache_with_expiry(876000)
def get_show(show_id: str):
	"""获取剧集详情

	Args:
		show_id (str): 剧集的tmdb_id

	Returns:
		_type_: 剧集详情
	"""
	with acquire_client_sync() as turso_client:
		# 查询电影详情
		rows = turso_client.execute(
			SELECT_SHOW_BY_ID, [show_id]).rows
		if len(rows) == 0:
			return None
		return rows[0]


def update_share_link(show_id: str, share_link: str):
	"""更新分享链接

	Args:
		show_id (int): 剧集的tmdb_id
		share_link (str): 分享链接
	"""
	with acquire_client_sync() as turso_client:
		turso_client.execute(UPDATE_SHOW_SHARE_LINK, {
			'show_id': show_id, 'share_link': share_link})
		# 清除缓存
		get_shows.cache_clear()
		get_show.cache_clear()


@cache.cache_with_expiry(876000)
def get_index():
	"""获取剧集索引

	Returns:
		_type_: 索引数据(base64编码)
	"""
	with acquire_client_sync() as turso_client:
		# 查询剧集索引
		rows = turso_client.execute(
			SELECT_LOCAL_SEARCH_BY_TYPE, ('show',)).rows
		if len(rows) == 0:
			return ''
		return rows[0]['b64_index']
