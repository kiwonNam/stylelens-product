from bson.objectid import ObjectId
from stylelens_product.database import DataBase

STATUS_TODO = 'todo'
STATUS_DOING = 'doing'
STATUS_DONE = 'done'


class Crawls(DataBase):
  def __init__(self):
    super(Crawls, self).__init__()
    self.crawls = self.db.crawls

  def add_crawl(self, crawl):
    crawl_id = None
    crawl['status'] = STATUS_TODO
    query = {"host_code": crawl['host_code'], "version_id": crawl["version_id"]}
    try:
      r = self.crawls.update_one(query,
                                  {"$set": crawl},
                                  upsert=True)
    except Exception as e:
      print(e)

    if 'upserted' in r.raw_result:
      crawl_id = str(r.raw_result['upserted'])

    return crawl_id

  def get_crawls(self,
                version_id,
                status=STATUS_TODO,
                offset=0, limit=100):
    query = {}
    query['version_id'] = version_id
    query['status'] = status
    try:
      r = self.crawls.find(query).skip(offset).limit(limit)
    except Exception as e:
      print(e)

    return list(r)

  def get_size_crawls(self,
                 version_id,
                 status=None,
                 offset=0, limit=100):
    query = {}
    query['version_id'] = version_id

    if status is not None:
      query['status'] = status

    try:
      count = self.crawls.find(query).count()
    except Exception as e:
      print(e)

    return count

  def update_crawl_by_host_code(self, host_code, crawl):
    try:
      r = self.crawls.update_one({"host_code": host_code},
                                  {"$set": crawl})
    except Exception as e:
      print(e)

    return r.modified_count

