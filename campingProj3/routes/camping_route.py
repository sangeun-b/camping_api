from flask import render_template, request, Blueprint
from campingProj3.camping.service import CampingService
import campingProj3.camping.service as service

cser = service.CampingService()

bp = Blueprint('camping', __name__, url_prefix='/camping')

@bp.route('/next/<pageNo>')
def nextPage(pageNo:int):
    pageNo = int(pageNo)
    clist = cser.getNextPage(pageNo)
    pageNo = clist[0]
    clist = clist[1]
    return render_template('index.html', clist=clist, pageNo=pageNo)

@bp.route('/pre/<pageNo>')
def prePage(pageNo:int):
    pageNo = int(pageNo)
    clist = cser.getPrePage(pageNo)
    pageNo = clist[0]
    clist = clist[1]
    return render_template('index.html', clist=clist, pageNo=pageNo)

@bp.route('/detail/<pageNo>/<facltNm>')
def detailPage(pageNo,facltNm):
    pageNo = int(pageNo)
    c = cser.getDetail(pageNo,facltNm)
    return render_template('detail.html', c=c)

clist = []
@bp.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    addr =request.form['keyword']
    type = request.form['type']
    print(addr)
    if type == 'name':
        clist = cser.getCampByName(keyword)
    else:
        clist = cser.getCampByaddr(addr)
    return render_template('campinglist.html', clist=clist)

@bp.route('/detail/<facltNm>')
def searchDetail(facltNm):
    c = cser.getDetailBySearch(facltNm)
    return render_template('detail.html',c=c)