from flask import Blueprint, request
from core.result import Result
from components.trakt import movie_handler, show_handler

# 创建蓝图
blueprint = Blueprint('trakt', __name__, url_prefix='/trakt')


# =========================电影================================


@blueprint.route('/movie')
def movies():
	"""分页获取电影列表

	Returns:
		_type_: 电影列表
	"""
	# 获取请求参数page和page_size
	curr_page = int(request.args.get('page', 1))
	page_size = int(request.args.get('page_size', 10))
	try:
		return Result.success(movie_handler.get_movies(curr_page, page_size))
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/movie/<movie_id>')
def movie(movie_id):
	"""获取电影详情

	Args:
		movie_id (str): 电影的tmdb_id

	Returns:
		_type_: 电影详情
	"""
	try:
		return Result.success(movie_handler.get_movie(movie_id))
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/update_movie_share_link', methods=['POST'])
def update_movie_share_link():
	"""更新电影分享链接 content-type为application/x-www-form-urlencoded

	Returns:
		_type_: 更新结果
	"""
	# 获取请求参数tmdb_id和share_link
	movie_id = request.form.get('movie_id')
	share_link = request.form.get('share_link')
	if not movie_id or not share_link:
		return Result.fail('movie_id和share_link不能为空')
	try:
		movie_handler.update_share_link(movie_id, share_link)
		return Result.success('更新成功')
	except Exception as e:
		return Result.fail(e)


# ==============================剧集===================================


@blueprint.route('/show')
def shows():
	"""分页获取剧集列表

	Returns:
		_type_: 剧集列表
	"""
	# 获取请求参数page和page_size
	curr_page = int(request.args.get('page', 1))
	page_size = int(request.args.get('page_size', 10))
	try:
		return Result.success(show_handler.get_shows(curr_page, page_size))
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/show/<show_id>')
def show(show_id):
	"""获取剧集详情

	Args:
		show_id (str): 剧集的tmdb_id

	Returns:
		_type_: 剧集详情
	"""
	try:
		return Result.success(show_handler.get_show(show_id))
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/update_show_share_link', methods=['POST'])
def update_show_share_link():
	"""更新剧集分享链接 content-type为application/x-www-form-urlencoded

	Returns:
		_type_: 更新结果
	"""
	# 获取请求参数tmdb_id和share_link
	show_id = request.form.get('show_id')
	share_link = request.form.get('share_link')
	if not show_id or not share_link:
		return Result.fail('show_id和share_link不能为空')
	try:
		show_handler.update_share_link(show_id, share_link)
		return Result.success('更新成功')
	except Exception as e:
		return Result.fail(e)


# ==============================common================================


@blueprint.route('/index')
def index():
	"""获取电影/剧集索引
	"""
	try:
		return Result.success({
			'movie': movie_handler.get_index(),
			'show': show_handler.get_index()
		})
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/refresh_movie_cache')
def refresh_movie_cache():
	"""刷新电影缓存
	"""
	try:
		movie_handler.get_movies.cache_clear()
		movie_handler.get_movie.cache_clear()
		movie_handler.get_index.cache_clear()
		return Result.success(msg='刷新movie缓存成功')
	except Exception as e:
		return Result.fail(e)


@blueprint.route('/refresh_show_cache')
def refresh_show_cache():
	"""刷新剧集缓存
	"""
	try:
		show_handler.get_shows.cache_clear()
		show_handler.get_show.cache_clear()
		show_handler.get_index.cache_clear()
		return Result.success(msg='刷新show缓存成功')
	except Exception as e:
		return Result.fail(e)
