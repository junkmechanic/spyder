from django.http import HttpResponse
from django.template import loader, RequestContext
from webwiki.spider import weave, root_nodes
import threading
import time


lock = threading.Lock()


def get_root_node():
    lock.acquire()
    root_node = root_nodes[1]
    lock.release()
    return root_node


def crawl_over():
    working = threading.Thread(target=weave)
    working.start()


def send_response(request):
    template_name = "web1.html"
    root_node = get_root_node()
    num_of_nodes = len(root_node.weighed_links)
    t = loader.get_template(template_name)
    c = RequestContext(request, {'root': root_node, 'num': num_of_nodes})
    return HttpResponse(t.render(c), content_type="application/xhtml+xml")


def buildweb(request):
    crawl_over()
    time.sleep(5)
    return send_response(request)


def refresh_page(request):
    return send_response(request)
