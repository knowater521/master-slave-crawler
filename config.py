list_url = 'http://podcasts.rthk.hk/podcast/item_all.php?pid=287&current_year=2013'
content_url_head = 'http://podcasts.rthk.hk/podcast/'
task_url_head = 'http://podcasts.rthk.hk/podcast/'
proxy='127.0.0.1:8087'
proxies = {
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}
down_folder = 'download\\2013' 