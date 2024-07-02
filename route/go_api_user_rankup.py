from .tool.func import *

async def api_user_rankup():
    other_set = {}
    other_set["ip"] = ip_check()
    
    func_name = sys._getframe().f_code.co_name
    if flask.request.method == 'PATCH':
        func_name += '_patch'

    return flask.Response(response = (await python_to_golang(func_name, other_set)), status = 200, mimetype = 'application/json')