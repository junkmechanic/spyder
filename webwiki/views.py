from django.http import HttpResponse
from django.template import loader, RequestContext
from webwiki.spider import weave, root_nodes
import threading
import time
#import math
import copy


lock = threading.Lock()


def get_root_node():
    lock.acquire()
    print(root_nodes)
    root_node = root_nodes[1]
    lock.release()
    return root_node


def crawl_over(query_url=None):
    working = threading.Thread(target=weave(query_url))
    working.start()


def send_response(request):
    template_name = "web1.html"
    root_node = get_root_node()
    num_of_nodes = len(root_node.weighed_links)
    root_links = copy.deepcopy(root_node.weighed_links)
    largest = 0
    for key in root_links.keys():
        if root_links[key] > 32:
            root_links[key] = 32
        if root_links[key] < 2.5:
            root_links[key] = 2.5
        if root_links[key] > largest:
            largest = root_links[key]
    largest = largest + 4
    for key in root_links.keys():
        root_links[key] = largest - root_links[key]
        #root_links[key] = math.exp(500 * (root_links[key]))
        root_links[key] = (0.5 * root_links[key]) + 3
    t = loader.get_template(template_name)
    c = RequestContext(request, {'root': root_links, 'num': num_of_nodes,
                                 'root_url': root_node.name})
    return HttpResponse(t.render(c), content_type="application/xhtml+xml")


def buildweb(request):
    crawl_over()
    time.sleep(8)
    return send_response(request)


def refresh_page(request):
    return send_response(request)


def spin_new_web(request, query_url):
    crawl_over(query_url)
    time.sleep(8)
    return send_response(request)
