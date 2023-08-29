def args(request):
    if request.method == "GET":
        return request.args
    if request.method == "POST":
        return request.get_json(force=True)
